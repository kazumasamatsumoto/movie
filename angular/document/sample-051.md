# #051 [(ngModel)] 双方向バインディング

## 概要
Angular v20における双方向データバインディングの実装方法を学びます。[(ngModel)]を使用してフォーム入力とコンポーネントプロパティを効率的に連動させる方法を解説します。

## 学習目標
- [(ngModel)]の基本的な使用方法を理解する
- 双方向バインディングの仕組みを把握する
- フォーム開発における実践的な活用方法を習得する

## 📺 画面表示用コード

```typescript
// コンポーネント
export class UserFormComponent {
  userName = '';
  email = '';
}
```

```html
<!-- テンプレート -->
<input [(ngModel)]="userName" placeholder="ユーザー名">
<input [(ngModel)]="email" placeholder="メールアドレス">

<p>入力値: {{userName}}</p>
<p>メール: {{email}}</p>
```

```typescript
// リアクティブな値の変更監視
onInputChange() {
  console.log('ユーザー名:', this.userName);
}
```

## 技術ポイント

### 1. 基本的な双方向バインディング
```typescript
export class UserFormComponent {
  userName = '';
  email = '';
}
```

```html
<input [(ngModel)]="userName" placeholder="ユーザー名">
<input [(ngModel)]="email" placeholder="メールアドレス">
```

### 2. リアクティブな値の監視
```typescript
onInputChange() {
  console.log('ユーザー名:', this.userName);
  console.log('メール:', this.email);
}
```

### 3. 値の表示
```html
<p>入力値: {{userName}}</p>
<p>メール: {{email}}</p>
```

## 実践的な活用例

### ユーザープロフィールフォーム
```typescript
export class ProfileFormComponent {
  profile = {
    name: '',
    email: '',
    age: 0,
    bio: ''
  };
  
  onSubmit() {
    console.log('送信データ:', this.profile);
  }
}
```

### リアルタイム検索
```typescript
export class SearchComponent {
  searchTerm = '';
  results: any[] = [];
  
  onSearchChange() {
    if (this.searchTerm.length > 2) {
      this.performSearch(this.searchTerm);
    }
  }
}
```

## ベストプラクティス

1. **初期値の設定**: プロパティには適切な初期値を設定する
2. **バリデーション**: 必要に応じてフォームバリデーションを追加する
3. **パフォーマンス**: 大量のデータがある場合はOnPush戦略を検討する
4. **型安全性**: TypeScriptの型定義を活用して安全性を向上させる

## 注意点

- FormsModuleのインポートが必須
- 複雑なロジックはコンポーネント側で処理
- パフォーマンスを考慮した実装を心がける
- Angular v20のSignalとの組み合わせも検討する

## 関連技術
- FormsModule
- テンプレート式
- プロパティバインディング
- イベントバインディング
