from datetime import date, datetime
from decimal import Decimal
from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


# --- Base Response ---
# A generic wrapper you can use for any endpoint that just returns
# a success/fail status with an optional message.

class BaseResponse(BaseModel):
    success: bool
    message: Optional[str] = None


# --- Enums ---
# Restricts a field to a fixed set of allowed string values.
# Inheriting from `str` keeps it JSON-serializable.

class DebtType(str, Enum):
    credit_card = "credit_card"
    student_loan = "student_loan"
    mortgage = "mortgage"
    personal_loan = "personal_loan"
    auto_loan = "auto_loan"
    medical = "medical"
    other = "other"


# --- Debt Schemas ---
# Pattern: Base → Create / Update / Read
#   Base:   shared fields (avoids repetition)
#   Create: what the client sends to CREATE a record
#   Update: what the client sends to partially UPDATE a record (all optional)
#   Read:   what the API returns (includes server-generated fields like id, timestamps)

class DebtBase(BaseModel):
    name: str
    debt_type: DebtType
    principal_amount: Decimal = Field(gt=0, description="Original loan amount")
    current_balance: Decimal = Field(ge=0, description="Remaining balance owed")
    interest_rate: float = Field(ge=0, le=100, description="Annual interest rate in percent")
    minimum_payment: Decimal = Field(ge=0, description="Minimum monthly payment")
    due_date: Optional[int] = Field(None, ge=1, le=31, description="Day of month payment is due")


class DebtCreate(DebtBase):
    # Inherits all fields from DebtBase.
    # Client sends this when POSTing a new debt.
    pass


class DebtUpdate(BaseModel):
    # All fields are Optional so the client only sends what changed (PATCH).
    name: Optional[str] = None
    current_balance: Optional[Decimal] = None
    interest_rate: Optional[float] = None
    minimum_payment: Optional[Decimal] = None
    due_date: Optional[int] = None


class DebtRead(DebtBase):
    # Returned by the API. Adds server-generated fields.
    id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}  # lets Pydantic read from SQLModel ORM objects


# --- Payment Schemas ---

class PaymentBase(BaseModel):
    amount: Decimal = Field(gt=0)
    payment_date: date
    notes: Optional[str] = None


class PaymentCreate(PaymentBase):
    debt_id: UUID  # links this payment to a specific debt


class PaymentRead(PaymentBase):
    id: UUID
    debt_id: UUID
    created_at: datetime

    model_config = {"from_attributes": True}


# --- AI Advisor Chat Schemas ---

class ChatRequest(BaseModel):
    message: str                                 # the user's question to Claude
    conversation_id: Optional[UUID] = None       # None = start a new conversation


class ChatResponse(BaseModel):
    conversation_id: UUID
    message: str                                 # Claude's reply
    suggestions: Optional[list[str]] = None      # optional follow-up action tips


class MessageRead(BaseModel):
    role: str       # "user" or "assistant"
    content: str
    created_at: datetime

    model_config = {"from_attributes": True}


# --- User / Summary Schemas ---

class UserRead(BaseModel):
    id: UUID
    email: str
    created_at: datetime


class DebtSummary(BaseModel):
    total_debt: Decimal
    total_minimum_payment: Decimal
    debts: list[DebtRead]
    highest_interest_debt: Optional[DebtRead] = None
    estimated_payoff_months: Optional[int] = None
