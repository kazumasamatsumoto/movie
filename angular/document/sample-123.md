# #123 「SignalInput vs @Input() 比較」

## 概要
Angular v20におけるSignalInputと@Input()の比較分析。それぞれの特徴と使い分けを理解し、適切な場面で最適な選択を行うことで、効率的で保守性の高いアプリケーションを構築する。

## 学習目標
- SignalInputと@Input()の特徴を理解する
- 適切な使い分けの基準を学ぶ
- 移行戦略を把握する

## 技術ポイント
- SignalInputのリアクティブ特性
- @Input()の従来的な動作
- computed()との連携
- パフォーマンスの違い

## 📺 画面表示用コード

### @Input() の実装
```typescript
@Component({
  selector: 'app-traditional-input',
  template: `
    <div>
      <h3>{{ user.firstName }} {{ user.lastName }}</h3>
      <p>年齢: {{ age }}</p>
    </div>
  `
})
export class TraditionalInputComponent {
  @Input() user: User = { firstName: '', lastName: '' };
  @Input() age: number = 0;
}
```

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
  user = input.required<User>();
  age = input(0);
  
  displayName = computed(() => 
    `${this.user().firstName} ${this.user().lastName}`
  );
  
  category = computed(() => {
    return this.age() < 18 ? '未成年' : '成人';
  });
}
```

### 使い分けの例
```typescript
// シンプルな値渡し → @Input()
@Component({
  template: `<div>{{ message }}</div>`
})
export class SimpleComponent {
  @Input() message: string = '';
}

// リアクティブな計算が必要 → SignalInput
@Component({
  template: `<div>{{ computedValue() }}</div>`
})
export class ReactiveComponent {
  data = input.required<Data>();
  
  computedValue = computed(() => 
    this.data().value * 2
  );
}
```

## 実践的な活用例
- 段階的なSignal移行
- パフォーマンスクリティカルな部分での使い分け
- レガシーコードとの共存

## ベストプラクティス
- 用途に応じて適切に選択する
- 段階的な移行を計画する
- パフォーマンステストを実施する
- チームでの統一ルールを決める

## 注意点
- SignalInputは新機能のため、学習コストがある
- 既存コードとの互換性を考慮する
- パフォーマンスの違いを理解する

## 関連技術
- Signal
- 変更検出戦略
- リアクティブプログラミング
- 移行戦略
