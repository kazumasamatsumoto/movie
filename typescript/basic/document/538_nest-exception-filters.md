# #538 「Nest.js例外フィルタ」

四国めたん「Nest.jsの例外フィルタでもneverが大活躍だよ。」
ずんだもん「AppExceptionを判別Unionにしてcatch()で全部処理してたね。」
四国めたん「validation/unauthorized/notfoundをifでハンドリングしてconst check: never = exception; を置く。」
ずんだもん「HttpErrorも400〜500を列挙してgetErrorMessage()で網羅してた。」
四国めたん「型に含まれないステータスを入れると即エラーになる。」
ずんだもん「DomainExceptionでもdomainごとにBadRequestやUnprocessableを返してたよ。」
四国めたん「最後のcheck: never = ex; で未知ドメインを検知する仕掛け。」
ずんだもん「例外処理の抜け漏れがなくなるのは安心だね。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: AppExceptionフィルタ */
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
/** Example 2: HTTPステータス処理 */
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
/** Example 3: ドメイン例外 */
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
