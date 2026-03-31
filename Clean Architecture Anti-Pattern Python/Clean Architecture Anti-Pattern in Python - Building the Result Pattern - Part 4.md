# Clean Architecture Anti-Pattern in Python - Building the Result Pattern - Part 4


## Introduction: The Foundation of Architectural Resilience

In **Part 1** of this series, we established the architectural violation of using exceptions for domain outcomes. In **Part 2**, we quantified the performance cost—23x slower execution and 12x more memory allocation. In **Part 3**, we provided the comprehensive taxonomy that distinguishes infrastructure exceptions from domain outcomes.

This story delivers the implementation: the complete Result pattern in Python 3.12+ that enables architectural separation, performance optimization, and explicit contracts.

The Result pattern is not merely a wrapper around exceptions. It is a functional approach to error handling that makes domain outcomes explicit, enables composition, and preserves infrastructure exceptions for their intended purpose. When combined with Python 3.12+ advanced features—dataclasses, generics, match statements, and async/await—the Result pattern becomes both elegant and powerful.

---

## Key Takeaways from Previous Stories

| Story | Key Takeaway |
|-------|--------------|
| **1. 🏛️ A Developer's Guide to Resilience - Part 1** | Domain exceptions at presentation boundaries violate Clean Architecture. The Result pattern restores proper layer separation. |
| **2. 🎭 Domain Logic in Disguise - Part 2** | Exceptions for domain outcomes are 23x slower and allocate 12x more memory than Result pattern failures in Python. |
| **3. 🔍 Defining the Boundary - Part 3** | Determinism distinguishes infrastructure (non-deterministic) from domain outcomes (deterministic). Clear taxonomy enables consistent classification. |

This story builds upon these principles by providing the complete, production-ready implementation of the Result pattern in Python 3.12+.

---

## 1. The Result Pattern Architecture

### 1.1 Core Concepts

The Result pattern consists of three fundamental components:

```mermaid
flowchart TD
    subgraph ResultPattern["Result Pattern Components"]
        A[Result[T]] --> B[Success State]
        A --> C[Failure State]
        
        B --> D[Contains Value]
        C --> E[Contains DomainError]
        
        F[DomainError] --> G[Error Code]
        F --> H[Error Message]
        F --> I[Error Type]
        F --> J[Metadata]
        
        K[Result Factory Methods] --> L[success]
        K --> M[failure]
        
        N[Functional Extensions] --> O[map]
        N --> P[tap]
        N --> Q[match]
        N --> R[bind]
    end
    
    style ResultPattern fill:#e1f5fe,stroke:#01579b
    style Result fill:#c8e6c9,stroke:#2e7d32
    style DomainError fill:#fff9c4,stroke:#fbc02d
```

### 1.2 Design Principles

| Principle | Implementation |
|-----------|----------------|
| **Immutability** | Result and DomainError are immutable after creation (frozen dataclasses) |
| **Explicit Failure** | No hidden exceptions; all outcomes declared in return type |
| **Functional Composition** | map, bind, and tap enable declarative pipelines |
| **Type Safety** | Generic Result[T] preserves type information via TypeVar |
| **Python 3.12+ Features** | match statements, dataclasses, generics, async/await |

---

## 2. Complete Result Type Implementation

### 2.1 Core Result[T] Implementation

```python
# domain/common/result.py
# Python 3.12+: Complete Result[T] implementation with functional extensions
# Design Pattern: Monad Pattern - Result[T] is a monad with bind/map operations
# SOLID: Single Responsibility - Result only handles success/failure state

from dataclasses import dataclass
from typing import Generic, TypeVar, Optional, Callable, Awaitable, Union, Any
from enum import Enum
import asyncio
import functools

T = TypeVar('T')
TResult = TypeVar('TResult')


class Result(Generic[T]):
    """
    Represents the result of an operation that can either succeed with a value
    or fail with a domain error.
    
    Design Pattern: Monad Pattern - provides map, bind, and match operations
    SOLID: Interface Segregation - clear contract with success/failure semantics
    """
    
    def __init__(self, is_success: bool, value: Optional[T] = None, error: Optional['DomainError'] = None):
        """
        Private constructor. Use success() or failure() factory methods.
        
        SOLID: Dependency Inversion - callers depend on factory methods, not constructor
        """
        self._is_success = is_success
        self._value = value
        self._error = error
    
    @classmethod
    def success(cls, value: T) -> 'Result[T]':
        """Creates a successful result with the given value."""
        return cls(True, value=value, error=None)
    
    @classmethod
    def failure(cls, error: 'DomainError') -> 'Result[T]':
        """Creates a failed result with the given domain error."""
        return cls(False, value=None, error=error)
    
    @property
    def is_success(self) -> bool:
        """Returns True if the operation succeeded."""
        return self._is_success
    
    @property
    def is_failure(self) -> bool:
        """Returns True if the operation failed."""
        return not self._is_success
    
    @property
    def value(self) -> T:
        """
        Gets the success value.
        
        SOLID: Liskov Substitution - consistent interface for success state
        """
        if not self._is_success:
            raise ValueError(f"Cannot access value of failed result: {self._error}")
        return self._value
    
    @property
    def error(self) -> 'DomainError':
        """
        Gets the error.
        
        SOLID: Liskov Substitution - consistent interface for failure state
        """
        if self._is_success:
            raise ValueError("Cannot access error of successful result")
        return self._error
    
    def match(
        self,
        on_success: Callable[[T], TResult],
        on_failure: Callable[['DomainError'], TResult]
    ) -> TResult:
        """
        Pattern matching for functional handling of success and failure.
        
        Design Pattern: Strategy Pattern - different strategies for success/failure
        SOLID: Open/Closed - new handling strategies added via callbacks
        """
        if self._is_success:
            return on_success(self._value)
        return on_failure(self._error)
    
    async def match_async(
        self,
        on_success: Callable[[T], Awaitable[TResult]],
        on_failure: Callable[['DomainError'], Awaitable[TResult]]
    ) -> TResult:
        """Async pattern matching for functional handling."""
        if self._is_success:
            return await on_success(self._value)
        return await on_failure(self._error)
    
    def map(self, mapper: Callable[[T], TResult]) -> 'Result[TResult]':
        """
        Transforms the success value if successful; otherwise propagates the failure.
        
        Design Pattern: Functor Pattern - map applies function to value
        """
        if self._is_success:
            return Result.success(mapper(self._value))
        return Result.failure(self._error)
    
    async def map_async(self, mapper: Callable[[T], Awaitable[TResult]]) -> 'Result[TResult]':
        """Async version of map."""
        if self._is_success:
            return Result.success(await mapper(self._value))
        return Result.failure(self._error)
    
    def bind(self, binder: Callable[[T], 'Result[TResult]']) -> 'Result[TResult]':
        """
        Binds a function that returns a Result to the success value.
        
        Design Pattern: Monad Pattern - bind (>>=) operation for composition
        SOLID: Dependency Inversion - depends on Result abstraction
        """
        if self._is_success:
            return binder(self._value)
        return Result.failure(self._error)
    
    async def bind_async(self, binder: Callable[[T], Awaitable['Result[TResult]']]) -> 'Result[TResult]':
        """Async version of bind."""
        if self._is_success:
            return await binder(self._value)
        return Result.failure(self._error)
    
    def tap(self, action: Callable[[T], Any]) -> 'Result[T]':
        """
        Executes an action on the success value without changing the result.
        
        Design Pattern: Tap Pattern - side effect without modifying flow
        SOLID: Single Responsibility - side effects separated from transformation
        """
        if self._is_success:
            action(self._value)
        return self
    
    async def tap_async(self, action: Callable[[T], Awaitable[Any]]) -> 'Result[T]':
        """Async version of tap."""
        if self._is_success:
            await action(self._value)
        return self
    
    def tap_error(self, action: Callable[['DomainError'], Any]) -> 'Result[T]':
        """Executes an action on the error value without changing the result."""
        if not self._is_success:
            action(self._error)
        return self
    
    def value_or(self, default: T) -> T:
        """Returns the success value or a default if failed."""
        return self._value if self._is_success else default
    
    def value_or_raise(self, exception_factory: Optional[Callable[['DomainError'], Exception]] = None) -> T:
        """
        Returns the success value or raises an exception if failed.
        
        Use sparingly - primarily for boundary layers where Result must convert to exception.
        """
        if self._is_success:
            return self._value
        
        if exception_factory:
            raise exception_factory(self._error)
        
        raise ValueError(f"Result failed: {self._error}")
    
    def to_optional(self) -> Optional[T]:
        """Converts to Optional[T] (None for failure)."""
        return self._value if self._is_success else None
    
    def __bool__(self) -> bool:
        """Returns True if the result is a success."""
        return self._is_success
    
    def __repr__(self) -> str:
        if self._is_success:
            return f"Result.success({self._value})"
        return f"Result.failure({self._error})"
    
    def __eq__(self, other: Any) -> bool:
        """Equality comparison for results."""
        if not isinstance(other, Result):
            return False
        
        if self._is_success != other._is_success:
            return False
        
        if self._is_success:
            return self._value == other._value
        return self._error == other._error
```

### 2.2 Static Result Helper Class

```python
# domain/common/result.py - Static helpers
# Design Pattern: Factory Pattern - static methods for creating results

import asyncio
from typing import List, Callable, Awaitable, TypeVar, Optional
import functools

T = TypeVar('T')


class ResultHelpers:
    """
    Static helpers for working with Result types.
    
    Design Pattern: Factory Pattern - provides factory methods for common scenarios
    SOLID: Single Responsibility - only handles result creation and composition
    """
    
    @staticmethod
    def success(value: T) -> Result[T]:
        """Creates a success result."""
        return Result.success(value)
    
    @staticmethod
    def failure(error: 'DomainError') -> Result[T]:
        """Creates a failure result."""
        return Result.failure(error)
    
    @staticmethod
    def from_optional(
        value: Optional[T],
        error_factory: Callable[[], 'DomainError']
    ) -> Result[T]:
        """
        Creates a result from an optional value.
        
        SOLID: Open/Closed - error factory allows custom error creation
        """
        if value is not None:
            return Result.success(value)
        return Result.failure(error_factory())
    
    @staticmethod
    async def from_try_async(
        coroutine: Awaitable[T],
        error_factory: Callable[[Exception], 'DomainError']
    ) -> Result[T]:
        """
        Converts a coroutine that might raise an exception to a Result.
        
        Design Pattern: Adapter Pattern - adapts exception-throwing code to Result
        """
        try:
            value = await coroutine
            return Result.success(value)
        except Exception as ex:
            return Result.failure(error_factory(ex))
    
    @staticmethod
    def from_try(
        func: Callable[[], T],
        error_factory: Callable[[Exception], 'DomainError']
    ) -> Result[T]:
        """Converts a function that might raise an exception to a Result."""
        try:
            value = func()
            return Result.success(value)
        except Exception as ex:
            return Result.failure(error_factory(ex))
    
    @staticmethod
    def combine(results: List[Result[T]]) -> Result[List[T]]:
        """
        Combines multiple results, returning the first failure or all successes.
        
        SOLID: Interface Segregation - combines multiple results into one
        """
        failures = [r for r in results if r.is_failure]
        if failures:
            return Result.failure(failures[0].error)
        
        return Result.success([r.value for r in results])
    
    @staticmethod
    async def combine_async(tasks: List[Awaitable[Result[T]]]) -> Result[List[T]]:
        """Async version of combine."""
        results = await asyncio.gather(*tasks)
        return ResultHelpers.combine(results)
    
    @staticmethod
    def traverse(
        items: List[T],
        func: Callable[[T], Result[TResult]]
    ) -> Result[List[TResult]]:
        """
        Applies a function that returns Result to each item.
        Returns first failure or list of successes.
        
        Design Pattern: Traversal Pattern - functional iteration over collections
        """
        results = []
        for item in items:
            result = func(item)
            if result.is_failure:
                return Result.failure(result.error)
            results.append(result.value)
        
        return Result.success(results)
    
    @staticmethod
    async def traverse_async(
        items: List[T],
        func: Callable[[T], Awaitable[Result[TResult]]]
    ) -> Result[List[TResult]]:
        """Async version of traverse."""
        results = []
        for item in items:
            result = await func(item)
            if result.is_failure:
                return Result.failure(result.error)
            results.append(result.value)
        
        return Result.success(results)
    
    @staticmethod
    def lift(value: T) -> Result[T]:
        """Lifts a value into a successful Result."""
        return Result.success(value)
    
    @staticmethod
    def lift_error(error: 'DomainError') -> Result[T]:
        """Lifts an error into a failed Result."""
        return Result.failure(error)


# Alias for convenience
ResultOk = Result.success
ResultErr = Result.failure
```

---

## 3. Complete DomainError Implementation

### 3.1 DomainError with Python 3.12+ Features

```python
# domain/common/domain_error.py
# Python 3.12+: Complete DomainError implementation
# Design Pattern: Factory Pattern - factory methods for all error types
# SOLID: Single Responsibility - DomainError only represents error data

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any, Dict, Optional, List
from datetime import datetime


class DomainErrorType(Enum):
    """Domain error types for HTTP status code mapping."""
    
    CONFLICT = auto()           # 409 - Duplicate, state conflict
    NOT_FOUND = auto()          # 404 - Resource missing
    VALIDATION = auto()         # 400 - Invalid input
    UNAUTHORIZED = auto()       # 401 - Authentication required
    FORBIDDEN = auto()          # 403 - Authorization denied
    BUSINESS_RULE = auto()      # 422 - Business rule violation
    GONE = auto()               # 410 - Resource no longer available
    TOO_MANY_REQUESTS = auto()  # 429 - Rate limiting
    QUOTA_EXCEEDED = auto()     # 429 - Account quota exceeded
    
    def to_http_status(self) -> int:
        """Maps domain error type to HTTP status code."""
        mapping = {
            DomainErrorType.CONFLICT: 409,
            DomainErrorType.NOT_FOUND: 404,
            DomainErrorType.VALIDATION: 400,
            DomainErrorType.UNAUTHORIZED: 401,
            DomainErrorType.FORBIDDEN: 403,
            DomainErrorType.BUSINESS_RULE: 422,
            DomainErrorType.GONE: 410,
            DomainErrorType.TOO_MANY_REQUESTS: 429,
            DomainErrorType.QUOTA_EXCEEDED: 429,
        }
        return mapping.get(self, 500)


@dataclass(frozen=True)
class DomainError:
    """
    Represents a domain error with code, message, type, and metadata.
    
    Design Pattern: Value Object - immutable, no identity
    SOLID: Single Responsibility - only represents error data, no logic beyond validation
    """
    
    code: str
    message: str
    type: DomainErrorType
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Validate error data."""
        if not self.code:
            raise ValueError("DomainError code cannot be empty")
        if not self.message:
            raise ValueError("DomainError message cannot be empty")
    
    def __str__(self) -> str:
        return f"[{self.code}] {self.message}"
    
    # ========================================================================
    # Resource State Errors
    # ========================================================================
    
    @classmethod
    def not_found(cls, resource_type: str, identifier: Any) -> 'DomainError':
        """Creates a not found error."""
        return cls(
            code=f"{resource_type.lower()}.not_found",
            message=f"{resource_type} with identifier '{identifier}' was not found",
            type=DomainErrorType.NOT_FOUND,
            metadata={"resource_type": resource_type, "identifier": str(identifier)}
        )
    
    @classmethod
    def conflict(cls, resource_type: str, reason: str, details: Any = None) -> 'DomainError':
        """Creates a conflict error."""
        metadata = {"resource_type": resource_type, "reason": reason}
        if details:
            metadata["details"] = details
        
        return cls(
            code=f"{resource_type.lower()}.conflict",
            message=f"{resource_type} conflict: {reason}",
            type=DomainErrorType.CONFLICT,
            metadata=metadata
        )
    
    @classmethod
    def gone(cls, resource_type: str, identifier: Any) -> 'DomainError':
        """Creates a gone (resource no longer available) error."""
        return cls(
            code=f"{resource_type.lower()}.gone",
            message=f"{resource_type} with identifier '{identifier}' is no longer available",
            type=DomainErrorType.GONE,
            metadata={"resource_type": resource_type, "identifier": str(identifier)}
        )
    
    # ========================================================================
    # Validation Errors
    # ========================================================================
    
    @classmethod
    def validation(cls, field: str, message: str) -> 'DomainError':
        """Creates a field-specific validation error."""
        return cls(
            code="validation.failed",
            message=message,
            type=DomainErrorType.VALIDATION,
            metadata={"field": field}
        )
    
    @classmethod
    def validation_multiple(cls, errors: Dict[str, str]) -> 'DomainError':
        """Creates a validation error with multiple fields."""
        return cls(
            code="validation.failed",
            message="One or more validation errors occurred",
            type=DomainErrorType.VALIDATION,
            metadata={"errors": errors}
        )
    
    # ========================================================================
    # Business Rule Errors
    # ========================================================================
    
    @classmethod
    def business_rule(cls, rule: str, message: str, context: Any = None) -> 'DomainError':
        """Creates a business rule violation error."""
        metadata = {}
        if context:
            metadata["context"] = context
        
        return cls(
            code=f"business.{rule.lower()}",
            message=message,
            type=DomainErrorType.BUSINESS_RULE,
            metadata=metadata
        )
    
    @classmethod
    def insufficient_funds(
        cls,
        available: float,
        required: float,
        currency: str = "USD"
    ) -> 'DomainError':
        """Creates an insufficient funds error."""
        return cls(
            code="business.insufficient_funds",
            message=f"Insufficient funds. Available: {currency} {available:.2f}, Required: {currency} {required:.2f}",
            type=DomainErrorType.BUSINESS_RULE,
            metadata={
                "available": available,
                "required": required,
                "currency": currency
            }
        )
    
    @classmethod
    def out_of_stock(
        cls,
        product_id: str,
        requested: int,
        available: int
    ) -> 'DomainError':
        """Creates an out of stock error."""
        return cls(
            code="business.out_of_stock",
            message=f"Product {product_id} out of stock. Requested: {requested}, Available: {available}",
            type=DomainErrorType.BUSINESS_RULE,
            metadata={
                "product_id": product_id,
                "requested": requested,
                "available": available
            }
        )
    
    @classmethod
    def duplicate(cls, entity_type: str, field: str, value: Any) -> 'DomainError':
        """Creates a duplicate entity error."""
        return cls(
            code=f"business.duplicate_{entity_type.lower()}",
            message=f"{entity_type} with {field} '{value}' already exists",
            type=DomainErrorType.CONFLICT,
            metadata={
                "entity_type": entity_type,
                "field": field,
                "value": value
            }
        )
    
    @classmethod
    def invalid_state(
        cls,
        entity_type: str,
        entity_id: Any,
        current_state: str,
        allowed_states: List[str]
    ) -> 'DomainError':
        """Creates an invalid state transition error."""
        return cls(
            code="business.invalid_state",
            message=f"{entity_type} {entity_id} cannot transition from {current_state}. Allowed: {allowed_states}",
            type=DomainErrorType.BUSINESS_RULE,
            metadata={
                "entity_type": entity_type,
                "entity_id": str(entity_id),
                "current_state": current_state,
                "allowed_states": allowed_states
            }
        )
    
    @classmethod
    def limit_exceeded(
        cls,
        entity_type: str,
        limit: float,
        current: float,
        period: str = "day"
    ) -> 'DomainError':
        """Creates a limit exceeded error."""
        return cls(
            code=f"business.{entity_type.lower()}_limit_exceeded",
            message=f"{entity_type} limit of {limit} per {period} exceeded. Current: {current}",
            type=DomainErrorType.BUSINESS_RULE,
            metadata={
                "entity_type": entity_type,
                "limit": limit,
                "current": current,
                "period": period
            }
        )
    
    # ========================================================================
    # Authorization Errors
    # ========================================================================
    
    @classmethod
    def unauthorized(cls, message: str = "Authentication required") -> 'DomainError':
        """Creates an unauthorized error."""
        return cls(
            code="auth.unauthorized",
            message=message,
            type=DomainErrorType.UNAUTHORIZED
        )
    
    @classmethod
    def forbidden(cls, resource: str, action: str, reason: str) -> 'DomainError':
        """Creates a forbidden error."""
        return cls(
            code="auth.forbidden",
            message=f"Access denied to {action} on {resource}: {reason}",
            type=DomainErrorType.FORBIDDEN,
            metadata={
                "resource": resource,
                "action": action,
                "reason": reason
            }
        )
    
    # ========================================================================
    # Capacity Errors
    # ========================================================================
    
    @classmethod
    def too_many_requests(
        cls,
        resource: str,
        limit: int,
        window_seconds: int
    ) -> 'DomainError':
        """Creates a rate limit exceeded error."""
        return cls(
            code="rate_limit.exceeded",
            message=f"Rate limit of {limit} requests per {window_seconds} seconds exceeded for {resource}",
            type=DomainErrorType.TOO_MANY_REQUESTS,
            metadata={
                "resource": resource,
                "limit": limit,
                "window_seconds": window_seconds
            }
        )
    
    @classmethod
    def quota_exceeded(cls, resource: str, limit: int, current: int) -> 'DomainError':
        """Creates a quota exceeded error."""
        return cls(
            code="quota.exceeded",
            message=f"{resource} quota exceeded. Limit: {limit}, Current: {current}",
            type=DomainErrorType.QUOTA_EXCEEDED,
            metadata={
                "resource": resource,
                "limit": limit,
                "current": current
            }
        )
```

---

## 4. Functional Extensions and Composition

### 4.1 LINQ-Style Query Extensions

```python
# domain/common/result_extensions.py
# Functional extensions for Result[T] composition
# Design Pattern: Monad Pattern - provides do-notation style composition

from typing import Callable, TypeVar, Awaitable, List
import asyncio

T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')


class ResultExtensions:
    """
    Functional extensions for Result[T] composition.
    
    Design Pattern: Monad Pattern - enables do-notation style composition
    SOLID: Open/Closed - extensions add functionality without modifying Result class
    """
    
    @staticmethod
    def select_many(
        source: Result[T],
        collection_selector: Callable[[T], Result[U]],
        result_selector: Callable[[T, U], V]
    ) -> Result[V]:
        """
        LINQ-style SelectMany for result composition.
        
        Usage:
            result = from customer in customer_result
                     from order in order_result
                     select OrderConfirmation(customer, order)
        """
        return source.bind(
            lambda s: collection_selector(s).map(
                lambda c: result_selector(s, c)
            )
        )
    
    @staticmethod
    def where(predicate: Callable[[T], bool], error: 'DomainError') -> Callable[[Result[T]], Result[T]]:
        """
        LINQ-style Where for result filtering.
        
        Returns a function that filters a result based on predicate.
        """
        def filter_result(source: Result[T]) -> Result[T]:
            if source.is_failure:
                return source
            
            if predicate(source.value):
                return source
            
            return Result.failure(error)
        
        return filter_result
    
    @staticmethod
    def do_notation() -> '_DoNotationBuilder':
        """
        Creates a do-notation builder for imperative-style monadic composition.
        
        Usage:
            result = await (do()
                .bind(lambda: get_customer(request.customer_id))
                .bind(lambda customer: get_product(request.product_id))
                .bind(lambda product, customer: create_order(customer, product))
                .run())
        """
        return _DoNotationBuilder()


class _DoNotationBuilder:
    """
    Do-notation builder for imperative-style monadic composition.
    
    Design Pattern: Builder Pattern - builds composed monadic operations
    """
    
    def __init__(self):
        self._steps = []
        self._values = {}
    
    def bind(self, func: Callable) -> '_DoNotationBuilder':
        """Adds a binding step to the composition."""
        self._steps.append(func)
        return self
    
    async def run(self) -> Result:
        """Executes the composed monadic operations."""
        for step in self._steps:
            # Determine number of arguments the step expects
            import inspect
            sig = inspect.signature(step)
            param_count = len(sig.parameters)
            
            if param_count == 0:
                result = step()
            else:
                # Pass previously bound values as arguments
                args = [self._values[name] for name in list(self._values.keys())[:param_count]]
                result = step(*args)
            
            # Handle async results
            if asyncio.iscoroutine(result):
                result = await result
            
            if result.is_failure:
                return result
            
            # Store the value with a generated name
            self._values[f"value_{len(self._values)}"] = result.value
        
        # Return the last result
        return result


# Convenience function
def do():
    """Entry point for do-notation."""
    return _DoNotationBuilder()


# Python 3.12+ match statement integration
def match_result(result: Result[T]) -> dict:
    """
    Helper for matching Result in Python 3.12+ match statements.
    
    Usage:
        match match_result(result):
            case {"success": order}:
                return Results.ok(order)
            case {"failure": error}:
                return Results.bad_request(error.message)
    """
    if result.is_success:
        return {"success": result.value}
    return {"failure": result.error}
```

---

## 5. Async Result Composition Examples

### 5.1 Composing Async Operations

```python
# domain/services/order_service_composed.py
# Example of composing async operations with Result pattern
# Design Pattern: Monad Pattern - sequential composition with bind

import asyncio
from typing import List
import logging

logger = logging.getLogger(__name__)


class OrderServiceComposed:
    """
    Order service demonstrating functional composition with Result pattern.
    
    Design Pattern: Monad Pattern - composition with bind/map
    SOLID: Dependency Inversion - depends on Result abstractions
    """
    
    def __init__(self, customer_repo, product_repo, order_repo, inventory_service):
        self._customer_repo = customer_repo
        self._product_repo = product_repo
        self._order_repo = order_repo
        self._inventory_service = inventory_service
    
    async def create_order(self, request) -> Result:
        """
        Creates an order using functional composition.
        
        Python 3.12+: Uses match statements for pattern matching
        """
        # Functional composition with bind
        result = await (
            ResultHelpers.from_try_async(
                self._customer_repo.get_by_id(request.customer_id),
                lambda ex: DomainError.not_found("Customer", request.customer_id)
            )
            .bind_async(lambda customer: self._validate_credit(customer, request))
            .bind_async(lambda _: self._validate_inventory(request.items))
            .bind_async(lambda _: self._create_order_entity(request))
            .bind_async(lambda order: self._save_order(order))
            .tap_async(lambda order: logger.info(f"Order {order.id} created"))
        )
        
        return result
    
    async def _validate_credit(self, customer, request) -> Result:
        """Validate customer credit."""
        total = sum(item.quantity * item.unit_price for item in request.items)
        
        if total <= customer.credit_limit:
            return Result.success(True)
        
        return Result.failure(
            DomainError.insufficient_funds(customer.credit_limit, total)
        )
    
    async def _validate_inventory(self, items: List) -> Result:
        """Validate inventory for all items."""
        for item in items:
            result = await self._inventory_service.check_availability(
                item.product_id, item.quantity
            )
            
            if result.is_failure:
                return result
            
            if not result.value.is_available:
                return Result.failure(
                    DomainError.out_of_stock(
                        str(item.product_id),
                        item.quantity,
                        result.value.available_quantity
                    )
                )
        
        return Result.success(True)
    
    async def _create_order_entity(self, request) -> Result:
        """Create order entity."""
        order = Order.create(
            customer_id=request.customer_id,
            items=request.items,
            shipping_address=request.shipping_address
        )
        return Result.success(order)
    
    async def _save_order(self, order: Order) -> Result:
        """Save order to repository."""
        try:
            await self._order_repo.add(order)
            await self._order_repo.save_changes()
            return Result.success(order)
        except Exception as ex:
            logger.error(f"Failed to save order: {ex}")
            return Result.failure(
                DomainError.business_rule(
                    "order.save_failed",
                    "Failed to save order. Please try again."
                )
            )


# Example of using the composed service
async def example_usage():
    """Example showing functional composition in action."""
    
    service = OrderServiceComposed(
        customer_repo=CustomerRepository(),
        product_repo=ProductRepository(),
        order_repo=OrderRepository(),
        inventory_service=InventoryService()
    )
    
    request = CreateOrderRequest(
        customer_id="123",
        items=[
            OrderItem(product_id="prod-1", quantity=2, unit_price=25.00)
        ],
        shipping_address=Address(street="123 Main St", city="Boston", zip="02101")
    )
    
    result = await service.create_order(request)
    
    # Python 3.12+ match statement for result handling
    match match_result(result):
        case {"success": order}:
            print(f"Order created: {order.id}")
        
        case {"failure": error}:
            print(f"Failed: {error.message}")
            
            # Handle specific error types
            match error.type:
                case DomainErrorType.NOT_FOUND:
                    print("Resource not found")
                case DomainErrorType.BUSINESS_RULE:
                    print(f"Business rule violation: {error.code}")
                case DomainErrorType.VALIDATION:
                    print(f"Validation error: {error.metadata.get('field')}")
```

---

## 6. API Endpoint Integration

### 6.1 FastAPI Integration with Result Pattern

```python
# api/routes/orders.py
# FastAPI endpoints with Result pattern
# Design Pattern: Adapter Pattern - adapts Result to HTTP responses

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from typing import Optional
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/orders", tags=["orders"])


class ResultToHTTPAdapter:
    """
    Adapts Result[T] to HTTP responses.
    
    Design Pattern: Adapter Pattern - converts Result to HTTP responses
    SOLID: Single Responsibility - only handles HTTP adaptation
    """
    
    @staticmethod
    def adapt(result: Result[T]) -> JSONResponse:
        """Convert Result to appropriate HTTP response."""
        
        # Python 3.12+ match statement for pattern matching
        match result:
            case Result(is_success=True, value=order):
                return JSONResponse(
                    status_code=status.HTTP_201_CREATED,
                    content={"id": str(order.id), "status": order.status.value}
                )
            
            case Result(is_success=False, error=error):
                return ResultToHTTPAdapter._handle_error(error)
    
    @staticmethod
    def _handle_error(error: DomainError) -> JSONResponse:
        """Handle domain error and return appropriate HTTP response."""
        
        # Python 3.12+ match statement on error type
        match error.type:
            case DomainErrorType.NOT_FOUND:
                return JSONResponse(
                    status_code=status.HTTP_404_NOT_FOUND,
                    content={
                        "error": error.code,
                        "message": error.message,
                        "type": "resource-not-found",
                        "metadata": error.metadata
                    }
                )
            
            case DomainErrorType.CONFLICT:
                return JSONResponse(
                    status_code=status.HTTP_409_CONFLICT,
                    content={
                        "error": error.code,
                        "message": error.message,
                        "type": "conflict",
                        "metadata": error.metadata
                    }
                )
            
            case DomainErrorType.VALIDATION:
                # Handle multiple validation errors
                if "errors" in error.metadata:
                    return JSONResponse(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        content={
                            "error": error.code,
                            "message": error.message,
                            "type": "validation-error",
                            "errors": error.metadata["errors"]
                        }
                    )
                
                return JSONResponse(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    content={
                        "error": error.code,
                        "message": error.message,
                        "type": "validation-error",
                        "field": error.metadata.get("field")
                    }
                )
            
            case DomainErrorType.BUSINESS_RULE:
                return JSONResponse(
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                    content={
                        "error": error.code,
                        "message": error.message,
                        "type": "business-rule-violation",
                        "metadata": error.metadata
                    }
                )
            
            case DomainErrorType.UNAUTHORIZED:
                return JSONResponse(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    content={
                        "error": error.code,
                        "message": error.message,
                        "type": "unauthorized"
                    }
                )
            
            case DomainErrorType.FORBIDDEN:
                return JSONResponse(
                    status_code=status.HTTP_403_FORBIDDEN,
                    content={
                        "error": error.code,
                        "message": error.message,
                        "type": "forbidden",
                        "metadata": error.metadata
                    }
                )
            
            case DomainErrorType.TOO_MANY_REQUESTS:
                return JSONResponse(
                    status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                    content={
                        "error": error.code,
                        "message": error.message,
                        "type": "rate-limited",
                        "metadata": error.metadata
                    },
                    headers={"Retry-After": str(error.metadata.get("window_seconds", 60))}
                )
            
            case _:
                return JSONResponse(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    content={
                        "error": error.code,
                        "message": error.message,
                        "type": "internal-error"
                    }
                )


@router.post(
    "/",
    response_model=OrderResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
        409: {"model": ErrorResponse},
        422: {"model": ErrorResponse},
        429: {"model": ErrorResponse},
        503: {"model": ErrorResponse}
    }
)
async def create_order(
    request: CreateOrderRequest,
    service: OrderService = Depends(get_order_service)
):
    """
    Creates a new order.
    
    Returns:
        - 201 Created with order details on success
        - 400 Bad Request for validation errors
        - 404 Not Found for missing resources
        - 409 Conflict for duplicate/state conflicts
        - 422 Unprocessable Entity for business rule violations
        - 429 Too Many Requests for rate limiting
    """
    result = await service.create_order(request)
    
    return ResultToHTTPAdapter.adapt(result)


@router.get(
    "/{order_id}",
    response_model=OrderResponse,
    responses={404: {"model": ErrorResponse}}
)
async def get_order(
    order_id: str,
    service: OrderService = Depends(get_order_service)
):
    """Retrieves an order by ID."""
    
    result = await service.get_by_id(order_id)
    
    return ResultToHTTPAdapter.adapt(result)


@router.post(
    "/{order_id}/cancel",
    response_model=OrderResponse,
    responses={
        400: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
        422: {"model": ErrorResponse}
    }
)
async def cancel_order(
    order_id: str,
    reason: CancelReason,
    service: OrderService = Depends(get_order_service)
):
    """Cancels an existing order."""
    
    result = await service.cancel_order(order_id, reason.text)
    
    return ResultToHTTPAdapter.adapt(result)
```

---

## 7. Repository Layer with Result Pattern

### 7.1 Repository Interface

```python
# domain/repositories/order_repository.py
# Repository pattern with Result[T] return types
# Design Pattern: Repository Pattern - abstracts data access

from abc import ABC, abstractmethod
from typing import Optional, List
from uuid import UUID


class OrderRepository(ABC):
    """
    Repository for Order aggregate.
    
    Design Pattern: Repository Pattern - abstracts data persistence
    SOLID: Interface Segregation - focused interface for order operations
    """
    
    @abstractmethod
    async def get_by_id(self, order_id: UUID) -> Result[Order]:
        """Get order by ID. Returns Result.failure if not found."""
        pass
    
    @abstractmethod
    async def get_by_customer_id(self, customer_id: UUID) -> Result[List[Order]]:
        """Get all orders for a customer."""
        pass
    
    @abstractmethod
    async def add(self, order: Order) -> Result[Order]:
        """Add a new order."""
        pass
    
    @abstractmethod
    async def update(self, order: Order) -> Result[Order]:
        """Update an existing order."""
        pass
    
    @abstractmethod
    async def delete(self, order_id: UUID) -> Result[bool]:
        """Delete an order."""
        pass
    
    @abstractmethod
    async def exists(self, order_id: UUID) -> Result[bool]:
        """Check if an order exists."""
        pass
    
    @abstractmethod
    async def has_active_order_conflict(
        self,
        customer_id: UUID,
        product_ids: List[UUID]
    ) -> Result[bool]:
        """Check for conflicting active orders."""
        pass
```

### 7.2 Repository Implementation

```python
# infrastructure/repositories/postgres_order_repository.py
# PostgreSQL implementation with Result pattern
# Design Pattern: Repository Pattern - concrete implementation

import asyncpg
from typing import Optional, List
from uuid import UUID
import logging

logger = logging.getLogger(__name__)


class PostgresOrderRepository(OrderRepository):
    """
    PostgreSQL implementation of OrderRepository.
    
    Design Pattern: Repository Pattern - concrete implementation
    SOLID: Liskov Substitution - substitutable for OrderRepository
    """
    
    def __init__(self, connection_pool: asyncpg.Pool):
        self._pool = connection_pool
    
    async def get_by_id(self, order_id: UUID) -> Result[Order]:
        try:
            async with self._pool.acquire() as conn:
                row = await conn.fetchrow(
                    "SELECT id, customer_id, status, created_at, total_value "
                    "FROM orders WHERE id = $1",
                    order_id
                )
                
                if row is None:
                    return Result.failure(
                        DomainError.not_found("Order", order_id)
                    )
                
                order = Order(
                    id=row["id"],
                    customer_id=row["customer_id"],
                    status=OrderStatus(row["status"]),
                    created_at=row["created_at"],
                    total_value=row["total_value"]
                )
                
                return Result.success(order)
                
        except asyncpg.exceptions.QueryCanceledError as ex:
            # Infrastructure exception - timeout
            logger.error(f"Database timeout getting order {order_id}: {ex}")
            raise DatabaseInfrastructureException(
                "Database timeout occurred",
                sql_error_number=-2,
                inner_exception=ex
            )
        
        except asyncpg.exceptions.ConnectionDoesNotExistError as ex:
            # Infrastructure exception - connection lost
            logger.warning(f"Database connection lost: {ex}")
            raise TransientInfrastructureException(
                "Database connection lost",
                error_code="DB_CONN_LOST",
                inner_exception=ex,
                retry_after=5
            )
        
        except Exception as ex:
            # Unknown error - log and re-raise
            logger.error(f"Unexpected database error: {ex}")
            raise
    
    async def add(self, order: Order) -> Result[Order]:
        try:
            async with self._pool.acquire() as conn:
                async with conn.transaction():
                    await conn.execute(
                        """
                        INSERT INTO orders (id, customer_id, status, created_at, total_value)
                        VALUES ($1, $2, $3, $4, $5)
                        """,
                        order.id,
                        order.customer_id,
                        order.status.value,
                        order.created_at,
                        order.total_value
                    )
                    
                    # Insert order items
                    for item in order.items:
                        await conn.execute(
                            """
                            INSERT INTO order_items (id, order_id, product_id, quantity, unit_price)
                            VALUES ($1, $2, $3, $4, $5)
                            """,
                            item.id,
                            order.id,
                            item.product_id,
                            item.quantity,
                            item.unit_price
                        )
                
                return Result.success(order)
                
        except asyncpg.exceptions.UniqueViolationError as ex:
            # Domain outcome - duplicate order
            if "order_number" in str(ex):
                return Result.failure(
                    DomainError.duplicate("Order", "order_number", order.order_number)
                )
            
            # Unknown unique violation - re-raise as infrastructure
            logger.error(f"Unexpected unique violation: {ex}")
            raise DatabaseInfrastructureException(
                "Unexpected unique constraint violation",
                sql_error_number=2627,
                inner_exception=ex
            )
        
        except asyncpg.exceptions.ForeignKeyViolationError as ex:
            # Domain outcome - referenced entity missing
            return Result.failure(
                DomainError.business_rule(
                    "reference_missing",
                    "Referenced customer or product does not exist"
                )
            )
        
        except asyncpg.exceptions.DeadlockDetectedError as ex:
            # Infrastructure exception - deadlock (transient)
            logger.warning(f"Deadlock detected adding order: {ex}")
            raise DatabaseInfrastructureException(
                "Database deadlock occurred",
                sql_error_number=1205,
                inner_exception=ex
            )
    
    async def update(self, order: Order) -> Result[Order]:
        try:
            async with self._pool.acquire() as conn:
                result = await conn.execute(
                    """
                    UPDATE orders
                    SET status = $2, updated_at = NOW()
                    WHERE id = $1
                    """,
                    order.id,
                    order.status.value
                )
                
                if result == "UPDATE 0":
                    return Result.failure(
                        DomainError.not_found("Order", order.id)
                    )
                
                return Result.success(order)
                
        except asyncpg.exceptions.DeadlockDetectedError as ex:
            raise DatabaseInfrastructureException(
                "Database deadlock occurred",
                sql_error_number=1205,
                inner_exception=ex
            )
    
    async def has_active_order_conflict(
        self,
        customer_id: UUID,
        product_ids: List[UUID]
    ) -> Result[bool]:
        try:
            async with self._pool.acquire() as conn:
                row = await conn.fetchval(
                    """
                    SELECT EXISTS (
                        SELECT 1 FROM orders o
                        JOIN order_items oi ON oi.order_id = o.id
                        WHERE o.customer_id = $1
                        AND oi.product_id = ANY($2)
                        AND o.status IN ('pending', 'confirmed')
                    )
                    """,
                    customer_id,
                    product_ids
                )
                
                return Result.success(row or False)
                
        except Exception as ex:
            logger.error(f"Error checking order conflict: {ex}")
            raise
```

---

## 8. Python 3.12+ Advanced Features

### 8.1 Using match Statements with Result

```python
# api/handlers.py
# Python 3.12+ match statements for result handling

from typing import Union


def handle_result(result: Result[Order]) -> dict:
    """
    Handle Result using Python 3.12+ match statement.
    
    Python 3.12+: Enhanced pattern matching with class patterns
    """
    
    # Python 3.12+ match statement with class patterns
    match result:
        case Result(is_success=True, value=order):
            return {"status": "success", "data": order.to_dict()}
        
        case Result(is_success=False, error=DomainError(type=DomainErrorType.NOT_FOUND)):
            return {"status": "error", "type": "not_found", "message": result.error.message}
        
        case Result(is_success=False, error=DomainError(type=DomainErrorType.CONFLICT)):
            return {"status": "error", "type": "conflict", "message": result.error.message}
        
        case Result(is_success=False, error=DomainError(type=DomainErrorType.VALIDATION, metadata={"field": field})):
            return {"status": "error", "type": "validation", "field": field, "message": result.error.message}
        
        case Result(is_success=False, error=error):
            return {"status": "error", "type": "unknown", "code": error.code, "message": error.message}


# Python 3.12+ match statement with guards
def handle_result_with_guards(result: Result[Order], user_role: str) -> dict:
    """Handle Result with guard conditions."""
    
    match result:
        case Result(is_success=True, value=order) if user_role == "admin":
            return {"status": "success", "admin_view": order.to_admin_dict()}
        
        case Result(is_success=True, value=order):
            return {"status": "success", "data": order.to_dict()}
        
        case Result(is_success=False, error=error) if error.type == DomainErrorType.NOT_FOUND:
            return {"status": "error", "type": "not_found"}
        
        case Result(is_success=False, error=error):
            return {"status": "error", "message": error.message}
```

### 8.2 Using TypeVar and Generic

```python
# domain/common/types.py
# Advanced type hints with TypeVar and Generic

from typing import TypeVar, Generic, Callable, Awaitable, Union
from typing_extensions import ParamSpec

T = TypeVar('T')
U = TypeVar('U')
P = ParamSpec('P')


# Covariant and contravariant type variables for better type safety
T_co = TypeVar('T_co', covariant=True)
T_contra = TypeVar('T_contra', contravariant=True)


class Functor(Generic[T_co]):
    """Functor type class for Result."""
    
    def map(self, f: Callable[[T_co], U]) -> 'Functor[U]':
        raise NotImplementedError


class Monad(Generic[T_co], Functor[T_co]):
    """Monad type class for Result."""
    
    def bind(self, f: Callable[[T_co], 'Monad[U]']) -> 'Monad[U]':
        raise NotImplementedError


# Type alias for Result functions
ResultFunction = Callable[..., Result[T]]


# Decorator for converting exception-throwing functions to Result-returning
def to_result(error_factory: Callable[[Exception], DomainError]) -> Callable[[Callable[P, T]], Callable[P, Result[T]]]:
    """
    Decorator that converts a function that may raise exceptions to a Result-returning function.
    
    Design Pattern: Decorator Pattern - wraps functions with exception handling
    """
    def decorator(func: Callable[P, T]) -> Callable[P, Result[T]]:
        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> Result[T]:
            try:
                value = func(*args, **kwargs)
                return Result.success(value)
            except Exception as ex:
                return Result.failure(error_factory(ex))
        
        return wrapper
    
    return decorator


# Usage
@to_result(lambda ex: DomainError.business_rule("external_error", str(ex)))
def call_external_service() -> dict:
    # May raise various exceptions
    response = httpx.get("https://api.example.com/data")
    response.raise_for_status()
    return response.json()
```

---

## What We Learned in This Story

| Concept | Key Takeaway |
|---------|--------------|
| **Result[T] Core** | Immutable type with is_success/is_failure properties, value/error accessors, and functional composition methods |
| **DomainError Record** | Complete error type with code, message, type, metadata, and factory methods for common scenarios |
| **Functional Extensions** | map, bind, tap, match, and do-notation enable declarative pipelines |
| **Async Support** | Async versions of all composition methods for async/await workflows |
| **Repository Integration** | Repositories return Result[T] for domain outcomes and raise infrastructure exceptions |
| **API Endpoint Mapping** | ProblemDetails responses with appropriate status codes based on DomainErrorType |
| **Python 3.12+ Features** | match statements, dataclasses, generics, and async/await streamline implementation |

---

## Design Patterns & SOLID Principles Summary

| Pattern / Principle | Application in This Story |
|---------------------|--------------------------|
| **Monad Pattern** | Result[T] provides map, bind, and match operations for functional composition |
| **Factory Pattern** | DomainError factory methods, Result.success/failure create instances |
| **Repository Pattern** | Abstracts data persistence with Result return types |
| **Adapter Pattern** | ResultToHTTPAdapter converts Result to HTTP responses |
| **Decorator Pattern** | to_result decorator converts exception-throwing functions |
| **Builder Pattern** | do-notation builder for imperative-style monadic composition |
| **Single Responsibility** | Each class has focused responsibility (Result, DomainError, adapters) |
| **Open/Closed** | New error types added via DomainError factory methods without modifying existing code |
| **Liskov Substitution** | All Results can be treated uniformly via the Result interface |
| **Interface Segregation** | Result[T] provides focused interface; separate adapters for HTTP |
| **Dependency Inversion** | Code depends on Result and DomainError abstractions, not concrete implementations |

---

## Next Story

The next story in the series applies the Result pattern across four real-world domains with complete case studies.

---

**5. 🏢 Clean Architecture Anti-Pattern in Python - Across Real-World Domains - Part 5** – Four complete case studies demonstrating the pattern across distinct business domains: Payment Processing (insufficient funds vs gateway timeout), Inventory Management (out of stock vs database deadlock), Healthcare Scheduling (double-booking vs EMR integration failure), and Logistics Tracking (delivery window violation vs GPS device offline). Each case study includes domain models, service implementations, and infrastructure integration patterns.

---

## References to Previous Stories

This story builds upon the principles established in:

**1. 🏛️ Clean Architecture Anti-Pattern in Python - A Developer's Guide to Resilience - Part 1** – Architectural violation, domain-infrastructure distinction, and decision framework.

**2. 🎭 Clean Architecture Anti-Pattern in Python - Domain Logic in Disguise - Part 2** – Performance implications and why expected outcomes should never raise exceptions.

**3. 🔍 Clean Architecture Anti-Pattern in Python - Defining the Boundary - Part 3** – Comprehensive taxonomy distinguishing infrastructure exceptions from domain outcomes.

Key concepts referenced and implemented:
- The architectural violation addressed through Result pattern contracts
- The performance optimization achieved by eliminating exceptions for domain outcomes
- The taxonomy applied through DomainErrorType classification
- Infrastructure exception handling preserved through try-except in infrastructure boundaries

---

## Series Overview

1. **🏛️ Clean Architecture Anti-Pattern in Python - A Developer's Guide to Resilience - Part 1** – Foundational principles, architectural violation, domain-infrastructure distinction, Result pattern, and decision framework.

2. **🎭 Clean Architecture Anti-Pattern in Python - Domain Logic in Disguise - Part 2** – Performance implications of exception-based domain logic. Stack trace overhead, memory profiling, GC pressure analysis, and why expected outcomes should never raise exceptions.

3. **🔍 Clean Architecture Anti-Pattern in Python - Defining the Boundary - Part 3** – Comprehensive taxonomy distinguishing infrastructure exceptions from domain outcomes. Decision matrices and classification patterns across all infrastructure layers.

4. **⚙️ Clean Architecture Anti-Pattern in Python - Building the Result Pattern - Part 4** – Complete implementation of Result<T> and DomainError with functional extensions. Python 3.12+ features, match statements, and async patterns. *(This Story)*

5. **🏢 Clean Architecture Anti-Pattern in Python - Across Real-World Domains - Part 5** – Four complete case studies: Payment Processing, Inventory Management, Healthcare Scheduling, and Logistics Tracking.

6. **🛡️ Clean Architecture Anti-Pattern in Python - Infrastructure Resilience - Part 6** – Global exception handling middleware, tenacity retry policies, circuit breakers, and health check integration.

7. **🧪 Clean Architecture Anti-Pattern in Python - Testing & Observability - Part 7** – Unit testing domain logic without exceptions (pytest), infrastructure failure testing, structured logging with structlog, and metrics with Prometheus.

8. **🚀 Clean Architecture Anti-Pattern in Python - The Road Ahead - Part 8** – Implementation checklist, migration strategies, Python 3.12+ roadmap, and long-term maintenance benefits.

---