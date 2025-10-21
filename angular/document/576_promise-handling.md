# #576 「Promise の処理」

## 概要
AsyncPipeはPromiseにも対応し、Promiseがresolveされた値をテンプレートで表示できる。一度解決したPromiseはキャッシュされる。

## 学習目標
- PromiseをAsyncPipeで扱う方法を理解する
- resolve後の再レンダリング挙動を把握する
- Observableとの違いを学ぶ

## 技術ポイント
- `{{ promise | async }}`
- resolve後の値が表示され、reject時はエラーとなる
- Promiseは一度解決すると再購読されない

## 📺 画面表示用コード（動画用）
```html
<p>{{ profilePromise | async }}</p>
```

## 💻 詳細実装例（学習用）
```typescript
protected readonly profilePromise = this.profileService.loadProfile();
```

```html
<h3>プロフィール: {{ profilePromise | async | json }}</h3>
```

## ベストプラクティス
- 単発の非同期処理はPromise + AsyncPipeで簡潔に
- 複数値やストリームはObservableで扱う
- Promiseがnullになるケースに備えて`*ngIf`でガード

## 注意点
- Promiseがrejectされるとエラーがスローされるためtry-catchやエラーハンドリングが必要
- Promiseは解決後の値をキャッシュするため、再評価されない点を理解
- 長時間かかるPromiseはユーザーにロード表示を提供

## 関連技術
- Observable
- Async/Await
- エラーハンドリング
