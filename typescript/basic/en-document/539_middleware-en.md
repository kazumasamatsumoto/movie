# #539 "Middleware"

Shikoku Metan: "Never keeps Nest middleware exhaustive."
Zundamon: "We processed json/form/multipart request types."
Shikoku Metan: "Unknown types hit const check: never = contentType;."
Zundamon: "authenticate() handled bearer/basic/apikey methods."
Shikoku Metan: "logRequest() walked debug/info/warn/error levels."
Zundamon: "Even with if chains never still guards us."
Shikoku Metan: "Middleware benefits hugely from type guards."
Zundamon: "Build failures remind us when to add branches."

---

## 📺 Code for Display

```typescript
/** Example 1: Request parsing */
type RequestType = "json" | "form" | "multipart";

@Injectable()
export class RequestParserMiddleware implements NestMiddleware {
  use(req: Request, res: Response, next: NextFunction) {
    const contentType = this.getRequestType(req);

    if (contentType === "json") return this.parseJson(req, next);
    if (contentType === "form") return this.parseForm(req, next);
    if (contentType === "multipart") return this.parseMultipart(req, next);
    const check: never = contentType;
    next();
  }
}
```

```typescript
/** Example 2: Authentication middleware */
type AuthMethod = "bearer" | "basic" | "apikey";

function authenticate(method: AuthMethod, req: Request): boolean {
  if (method === "bearer") return validateBearer(req);
  if (method === "basic") return validateBasic(req);
  if (method === "apikey") return validateApiKey(req);
  const check: never = method;
  return false;
}
```

```typescript
/** Example 3: Logging */
type LogLevel = "debug" | "info" | "warn" | "error";

function logRequest(level: LogLevel, message: string) {
  if (level === "debug") return logger.debug(message);
  if (level === "info") return logger.info(message);
  if (level === "warn") return logger.warn(message);
  if (level === "error") return logger.error(message);
  const check: never = level;
}
```
