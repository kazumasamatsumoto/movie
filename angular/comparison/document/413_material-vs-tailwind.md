# #413 「Angular Material vs Tailwind CSS あなたはどっち派？」

## 概要
Angular Materialは品質保証済みUIセットで素早く統一感を出せる。Tailwindはデザイン自由度とビルド時の最適化が強い。併用も視野に入れる。

## 学習目標
- Angular Materialの構成と得意なシナリオを整理する
- Tailwind CSSの採用メリットを理解する
- プロジェクト条件に応じた使い分け基準を決める

## 技術ポイント
- Angular Materialを成り立たせる主要API/構成要素
- Tailwind CSSで押さえる設定やコード記述
- 両者を共存・移行させるためのブリッジ手法

## 📺 画面表示用コード（動画用）
**Material派：完成度の高いUIキット**
```typescript
@Component({
  selector: 'app-login',
  standalone: true,
  imports: [MatButtonModule, MatFormFieldModule, MatInputModule],
  template: `
    <mat-form-field>
      <mat-label>Email</mat-label>
      <input matInput />
    </mat-form-field>
    <button mat-raised-button color="primary">Login</button>
  `,
})
export class LoginComponent {}
```

**Tailwind派：ユーティリティで柔軟に**
```typescript
<form class="space-y-3">
  <label class="block text-sm font-medium text-slate-500">Email</label>
  <input class="w-full rounded border px-3 py-2 focus:ring-2 focus:ring-emerald-500" />
  <button class="w-full rounded bg-emerald-500 py-2 font-semibold text-white">Login</button>
</form>
```

## 💻 詳細実装例（学習用）
```typescript
// tailwind.config.cjs
module.exports = {
  content: ['./src/**/*.{html,ts}'],
  theme: { extend: {} },
  plugins: [],
};
```

## ベストプラクティス
- Materialはデータ入力やアクセシビリティ要件が厳しい画面で採用し、テーマをFigmaと連携して管理する
- Tailwindはデザイントークンを`tailwind.config`にまとめ、クラス乱立を防ぐ
- 二者併用時はCSS変数・フォント設定を共通レイヤーに置き、重複を避ける

## 注意点
- Materialコンポーネントはバンドルサイズが大きくなるので`standalone`インポートで必要分だけ使う
- Tailwindはクラス名が長くなりがちなので`@apply`や部品化ルールを決める
- Design Systemの方針が揺れると両者のメンテが二重になるため意思決定を明確にする

## 関連技術
- Angular Material 3
- Tailwind CSS
- Design System
