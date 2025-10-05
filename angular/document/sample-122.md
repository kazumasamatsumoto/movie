# #122 「SignalInput - signal() ベース入力」

## 概要
Angular v20の新機能であるSignalInputの実装方法。signal()ベースの入力プロパティにより、リアクティブなSignalとして扱え、computed()での自動計算が可能な効率的な入力システムを実現する。

## 学習目標
- SignalInputの基本的な使い方を理解する
- 従来の@Input()との違いを把握する
- Signalとの連携による効率的な実装を学ぶ

## 技術ポイント
- input() 関数によるSignalInputの実装
- computed() との連携
- リアクティブな変更検出
- 型安全性の向上

## 📺 画面表示用コード

### SignalInput の実装
```typescript
@Component({
  selector: 'app-signal-input',
  template: `
    <div>
      <h3>{{ displayName() }}</h3>
      <p>年齢: {{ age() }}</p>
      <p>カテゴリ: {{ category() }}</p>
    </div>
  `
})
export class SignalInputComponent {
  // SignalInput の定義
  user = input.required<User>();
  age = input(0);
  
  // computed() での自動計算
  displayName = computed(() => 
    `${this.user().firstName} ${this.user().lastName}`
  );
  
  category = computed(() => {
    const userAge = this.age();
    if (userAge < 18) return '未成年';
    if (userAge < 65) return '成人';
    return '高齢者';
  });
}
```

### 使用例
```typescript
@Component({
  template: `
    <app-signal-input 
      [user]="currentUser"
      [age]="userAge">
    </app-signal-input>
  `
})
export class ParentComponent {
  currentUser = { firstName: 'John', lastName: 'Doe' };
  userAge = 25;
}
```

## 実践的な活用例
- ユーザープロフィール表示
- 商品情報の計算表示
- 動的なフォームバリデーション

## ベストプラクティス
- input.required() で必須プロパティを明示する
- computed() を活用した効率的な計算
- 適切な型定義を使用する
- 不要な再計算を避ける

## 注意点
- SignalInputはAngular v20の新機能
- 段階的な移行を検討する
- パフォーマンスを考慮した実装

## 関連技術
- Signal
- computed()
- リアクティブプログラミング
- 変更検出最適化
