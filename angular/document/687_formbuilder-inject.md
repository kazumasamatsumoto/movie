# #687 「inject(FormBuilder) での取得」

## 概要
inject(FormBuilder)はAngular v14以降で利用できる新しい依存注入記法で、コンストラクタを簡潔に保ちながらサービスを取得できる。

## 学習目標
- inject記法の使い方を理解する
- 従来のコンストラクタDIとの違いを把握する
- テストでの利用方法を学ぶ

## 技術ポイント
- injectは関数呼び出しで依存を返す
- コンポーネント外でもDIが利用できる
- TestBed.injectとの組み合わせでテストしやすい

## 📺 画面表示用コード（動画用）
```typescript
protected readonly fb = inject(FormBuilder);
```

## 💻 詳細実装例（学習用）
```typescript
const fb = inject(FormBuilder);

export class ExampleService {
  private readonly form = fb.group({
    name: fb.control('')
  });
}
```

## ベストプラクティス
- スタンドアロンコンポーネントではinjectを積極的に使う
- 複数箇所で利用する場合はヘルパー関数にまとめる
- テストではTestBed.injectで同じ記法を再現する

## 注意点
- injectはトップレベルまたはクラスフィールドで使用する
- コンストラクタDIと混在させる場合は順序に注意
- DIコンテキスト外で呼び出すと例外になる

## 関連技術
- inject関数
- 依存注入
- スタンドアロン
