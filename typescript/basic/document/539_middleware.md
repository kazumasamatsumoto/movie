# #539 「ミドルウェア」

四国めたん「Nestミドルウェアでもneverで分岐漏れを防げるよ。」
ずんだもん「RequestTypeを判定してjson/form/multipartを全部処理してたね。」
四国めたん「contentTypeが未知ならconst check: never = contentType; で警告。」
ずんだもん「認証ミドルウェアのauthenticate()もbearer/basic/apikeyを網羅してた。」
四国めたん「LogLevelのlogRequest()もdebug/info/warn/errorを順番に呼んでたよ。」
ずんだもん「switchじゃなくifチェーンでもneverを置けば安心だね。」
四国めたん「ミドルウェア層こそ型ガードで安全性を高めよう。」
ずんだもん「分岐追加をビルドが教えてくれるのは心強い。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: リクエストの解析 */
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
/** Example 2: 認証ミドルウェア */
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
/** Example 3: ロギング */
type LogLevel = "debug" | "info" | "warn" | "error";

function logRequest(level: LogLevel, message: string) {
  if (level === "debug") return logger.debug(message);
  if (level === "info") return logger.info(message);
  if (level === "warn") return logger.warn(message);
  if (level === "error") return logger.error(message);
  const check: never = level;
}
```
