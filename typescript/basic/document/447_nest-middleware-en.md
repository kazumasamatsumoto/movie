# #447 "Middleware"

Shikoku Metan: "Nest.js middleware methods use use(): void."
Zundamon: "LoggerMiddleware logged requests and called next()."
Shikoku Metan: "AuthMiddleware verified headers and threw when missing."
Zundamon: "CorsMiddleware set response headers too!"
Shikoku Metan: "Middleware performs side effects then hands control to next()."
Zundamon: "Void returns keep the Express-style flow clear."
Shikoku Metan: "Use void to highlight each middleware's responsibility."
Zundamon: "I'll keep Nest middleware void!"

---

## 📺 Code for Display

```typescript
/** Example 1: Logger middleware */
@Injectable()
export class LoggerMiddleware implements NestMiddleware {
  use(req: Request, res: Response, next: NextFunction): void {
    console.log(`${req.method} ${req.url}`);
    next();
  }
}

/** Example 2: Auth middleware */
@Injectable()
export class AuthMiddleware implements NestMiddleware {
  use(req: Request, res: Response, next: NextFunction): void {
    if (!req.headers.authorization) {
      throw new UnauthorizedException();
    }
    next();
  }
}

/** Example 3: CORS middleware */
@Injectable()
export class CorsMiddleware implements NestMiddleware {
  use(req: Request, res: Response, next: NextFunction): void {
    res.setHeader('Access-Control-Allow-Origin', '*');
    next();
  }
}
```
