# #447 「ミドルウェア」

四国めたん「Nest.jsのミドルウェアもuse(): voidで宣言します。」
ずんだもん「LoggerMiddlewareはリクエストをログしてnext()を呼んでいたね。」
四国めたん「AuthMiddlewareではheaderをチェックして未認証なら例外です。」
ずんだもん「CorsMiddlewareでヘッダーを設定する例もあった!」
四国めたん「useは副作用だけを実行してnext()へ制御を渡します。」
ずんだもん「戻り値が無いことでExpress互換のフローが分かりやすいね。」
四国めたん「voidでミドルウェアの責務を明確にしましょう。」
ずんだもん「Nest.jsミドルウェアもvoidで統一するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: LoggerMiddleware */
@Injectable()
export class LoggerMiddleware implements NestMiddleware {
  use(req: Request, res: Response, next: NextFunction): void {
    console.log(`${req.method} ${req.url}`);
    next();
  }
}

/** Example 2: 認証ミドルウェア */
@Injectable()
export class AuthMiddleware implements NestMiddleware {
  use(req: Request, res: Response, next: NextFunction): void {
    if (!req.headers.authorization) {
      throw new UnauthorizedException();
    }
    next();
  }
}

/** Example 3: CORSミドルウェア */
@Injectable()
export class CorsMiddleware implements NestMiddleware {
  use(req: Request, res: Response, next: NextFunction): void {
    res.setHeader('Access-Control-Allow-Origin', '*');
    next();
  }
}
```
