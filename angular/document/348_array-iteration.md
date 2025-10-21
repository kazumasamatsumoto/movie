# #348 「配列の反復処理」

## 概要
配列を反復するときは`*ngFor`と不変データの組み合わせが推奨され、変更検知との親和性が高い。

## 学習目標
- 配列操作とAngularの変更検知の関係を理解する
- 不変更新とtrackByを活用したパターンを学ぶ
- 配列変換ロジックをコンポーネントで完結させる

## 技術ポイント
- `items = [...items, newItem]`のように不変更新
- フィルタ・ソート済み配列をSignalやgetterで提供
- trackByでIDを返し、DOM再利用を促進

## 📺 画面表示用コード（動画用）
```html
<li *ngFor="let log of logs; trackBy: trackById">
  {{ log.message }}
</li>
```

## 💻 詳細実装例（学習用）
```typescript
interface LogEntry {
  id: number;
  message: string;
}

@Component({
  selector: 'app-array-iteration-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <button type="button" (click)="add()">ログ追加</button>
    <ul>
      <li *ngFor="let log of logs(); trackBy: trackById">{{ log.message }}</li>
    </ul>
  `
})
export class ArrayIterationDemoComponent {
  private readonly logsSignal = signal<LogEntry[]>([]);
  protected logs = this.logsSignal.asReadonly();
  private nextId = 1;

  protected add(): void {
    this.logsSignal.update(list => [...list, { id: this.nextId++, message: 'ログ追加' }]);
  }

  protected trackById(_: number, entry: LogEntry): number {
    return entry.id;
  }
}
```

## ベストプラクティス
- 配列操作はSignalやサービスで集中管理し、テンプレートでは参照のみ行う
- trackByで一意キーを返し、変更検知時の再描画を抑える
- 長いリストは仮想スクロールや分割描画を検討する

## 注意点
- 直接`push`すると同じ配列参照のままでOnPushコンポーネントが更新されない可能性がある
- trackBy未設定だとAngularがアイテムを比較するためコストが高い
- ソートやフィルタはステートレス関数で行い、副作用を避ける

## 関連技術
- Angular Signals
- trackBy
- CDK Virtual Scroll
