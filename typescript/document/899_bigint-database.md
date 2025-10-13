# #899 「データベース」

四国めたん「データベースのbigint型とTypeScriptのBigIntを連携させましょう。」
ずんだもん「PostgreSQLやMySQLのBIGINTは文字列で受け取るORMが多いよね。」
四国めたん「はい、型変換をカスタムしてBigIntに戻す必要があります。」
ずんだもん「PrismaやTypeORMではtransformerを定義すると楽だよ。」
四国めたん「精度を保ったままシリアライザを通してAPIへ渡しましょう。」
ずんだもん「DBとの橋渡しでもBigIntを活用してね！」
四国めたん「マイグレーション時の型設定も確認してください。」
ずんだもん「データ層での精度を守ろう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Prisma */
// schema.prisma
// model Account {
//   id BigInt @id @default(autoincrement())
//   balance BigInt
// }

/** Example 2: TypeORM transformer */
import { ValueTransformer } from "typeorm";
export const bigintTransformer: ValueTransformer = {
  to: (value?: bigint) => value?.toString(),
  from: (value?: string) => (value ? BigInt(value) : undefined),
};

/** Example 3: Repository */
const account = await repository.findOne({ where: { id: 1n } });
```
