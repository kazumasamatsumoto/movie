# #634 「DTOパターンで型を固定」

四国めたん「DTOパターンはunknownな入力を型安全に固定する要です」
ずんだもん「クラスやinterfaceで明示的に形を決めるんだよね」
四国めたん「はい。ValidationPipeや手動ガードでDTOへ変換します」
ずんだもん「レスポンスDTOを用意すると外部公開の契約も明確になるよ」
四国めたん「DTOの定義がanyを排除する第一歩です」
ずんだもん「チームでDTO運用を徹底しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: リクエストDTO */
export class CreateArticleDto {
  @IsString()
  title!: string;

  @IsString()
  body!: string;
}

/** Example 2: レスポンスDTO */
export interface ArticleResponse {
  id: number;
  title: string;
  body: string;
}

/** Example 3: マッピング */
function toArticleResponse(entity: ArticleEntity): ArticleResponse {
  return { id: entity.id, title: entity.title, body: entity.body };
}
```
