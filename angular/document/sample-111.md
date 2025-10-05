# #111 「@Input() + @Output() の組み合わせ」

## 概要
Angular v20における親子コンポーネント間の基本的な通信パターン。@Input()で親から子へデータを渡し、@Output()で子から親へイベントを送信する標準的な実装方法。

## 学習目標
- @Input()と@Output()の基本的な使い方を理解する
- 親子コンポーネント間のデータフローを把握する
- 再利用可能なコンポーネント設計を学ぶ

## 技術ポイント
- @Input()デコレータによるプロパティバインディング
- @Output()デコレータによるイベントエミッター
- EventEmitterを使った親へのイベント通知
- 型安全性を考慮した実装

## 📺 画面表示用コード

### 子コンポーネント
```typescript
@Component({
  selector: 'app-child',
  template: `
    <div>{{ message }}</div>
    <button (click)="sendMessage()">送信</button>
  `
})
export class ChildComponent {
  @Input() message: string = '';
  @Output() messageChange = new EventEmitter<string>();

  sendMessage() {
    this.messageChange.emit('Hello Parent!');
  }
}
```

### 親コンポーネント
```typescript
@Component({
  template: `
    <app-child 
      [message]="parentMessage"
      (messageChange)="onMessageChange($event)">
    </app-child>
  `
})
export class ParentComponent {
  parentMessage = 'Hello from Parent';

  onMessageChange(message: string) {
    console.log('Received:', message);
  }
}
```

## 実践的な活用例
- カスタムフォームコンポーネントの実装
- モーダルダイアログの表示制御
- リストアイテムの選択状態管理

## ベストプラクティス
- @Input()プロパティは読み取り専用として扱う
- @Output()イベント名は動詞形で命名する
- 型定義を明確にし、型安全性を保つ

## 注意点
- 子コンポーネントで@Input()プロパティを直接変更しない
- 大量のデータを@Input()で渡す場合はパフォーマンスを考慮する
- イベント名はキャメルケースで統一する

## 関連技術
- Component通信パターン
- プロパティバインディング
- イベントバインディング
- TypeScript型定義
