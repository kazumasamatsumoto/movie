# #112 「双方向バインディングのカスタム実装」

## 概要
Angular v20で独自の双方向バインディングを実装する方法。@Input()と@Output()を組み合わせて、[(ngModel)]と同様の双方向データバインディングをカスタムプロパティで実現する。

## 学習目標
- カスタム双方向バインディングの実装方法を理解する
- @Input()と@Output()の命名規則を把握する
- 再利用可能な双方向バインディングコンポーネントを設計する

## 技術ポイント
- @Input()プロパティの命名（例：value）
- @Output()イベントの命名（例：valueChange）
- 双方向バインディングの構文[(property)]
- 内部状態と外部状態の同期

## 📺 画面表示用コード

### カスタム入力コンポーネント
```typescript
@Component({
  selector: 'app-custom-input',
  template: `
    <input 
      [value]="value"
      (input)="onInput($event)">
  `
})
export class CustomInputComponent {
  @Input() value: string = '';
  @Output() valueChange = new EventEmitter<string>();

  onInput(event: Event) {
    const target = event.target as HTMLInputElement;
    this.valueChange.emit(target.value);
  }
}
```

### 使用例
```typescript
@Component({
  template: `
    <app-custom-input [(value)]="userName"></app-custom-input>
    <p>入力値: {{ userName }}</p>
  `
})
export class AppComponent {
  userName = 'Angular v20';
}
```

## 実践的な活用例
- カスタムスライダーコンポーネント
- 独自のセレクトボックス
- カスタムチェックボックス

## ベストプラクティス
- プロパティ名とイベント名の命名規則を統一する
- 内部状態と外部状態の整合性を保つ
- アクセシビリティを考慮した実装

## 注意点
- プロパティ名とイベント名の関係性を明確にする
- 無限ループを避けるため、値の変更時に条件チェックを行う
- パフォーマンスを考慮し、不要な再レンダリングを防ぐ

## 関連技術
- 双方向データバインディング
- カスタムディレクティブ
- フォームコントロール
- イベント処理
