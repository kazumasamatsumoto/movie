# #538 "Nest.js Exception Filters"

Shikoku Metan: "Never shines inside Nest.js exception filters."
Zundamon: "AppException was a discriminated union and catch() handled every type."
Shikoku Metan: "After validation/unauthorized/notfound we still add const check: never = exception;."
Zundamon: "HttpError listed 400-500 and getErrorMessage() covered them all."
Shikoku Metan: "Passing an unknown status fails at compile time."
Zundamon: "DomainException mapped domains to specific HTTP errors."
Shikoku Metan: "check: never = ex; exposes unknown domains immediately."
Zundamon: "No more gaps in exception handling."

---

## 📺 Code for Display

```typescript
/** Example 1: AppException filter */
type AppException =
  | { type: "validation"; errors: string[] }
  | { type: "unauthorized"; message: string }
  | { type: "notfound"; resource: string };

@Catch()
export class AllExceptionsFilter implements ExceptionFilter {
  catch(exception: AppException, host: ArgumentsHost) {
    if (exception.type === "validation") return this.handleValidation(exception);
    if (exception.type === "unauthorized") return this.handleUnauth(exception);
    if (exception.type === "notfound") return this.handleNotFound(exception);
    const check: never = exception;
  }
}
```

```typescript
/** Example 2: HTTP status handling */
type HttpError = 400 | 401 | 403 | 404 | 500;

function getErrorMessage(status: HttpError): string {
  if (status === 400) return "Bad Request";
  if (status === 401) return "Unauthorized";
  if (status === 403) return "Forbidden";
  if (status === 404) return "Not Found";
  if (status === 500) return "Internal Server Error";
  const check: never = status;
  return "Unknown Error";
}
```

```typescript
/** Example 3: Domain exceptions */
type DomainException =
  | { domain: "user"; code: "NOT_FOUND" | "DUPLICATE" }
  | { domain: "order"; code: "INVALID" | "EXPIRED" };

function handleException(ex: DomainException): HttpException {
  if (ex.domain === "user") return new BadRequestException(ex.code);
  if (ex.domain === "order") return new UnprocessableEntityException(ex.code);
  const check: never = ex;
  throw new InternalServerErrorException();
}
```
