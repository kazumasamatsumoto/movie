# #303 「Component Directive - コンポーネント」

## 概要
Component Directiveはテンプレートとスタイルを持つUI断片を再利用するためのAngularコンポーネントで、スタンドアロン化により依存関係を最小限に抑えられる。

## 学習目標
- Component Directiveの定義と責務を理解する
- standaloneコンポーネントとして宣言する手順を把握する
- Input/Outputによるインターフェース設計を学ぶ

## 技術ポイント
- `@Component`デコレータと`standalone: true`
- `imports`プロパティで依存ディレクティブを宣言
- `@Input`/`@Output`でUI部品の契約を構築

## 📺 画面表示用コード（動画用）
```typescript
@Component({
  selector: 'app-pill',
  standalone: true,
  template: `<span class="pill"><ng-content /></span>`
})
export class PillComponent {}
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-pill',
  standalone: true,
  imports: [CommonModule],
  template: `
    <span class="pill" [class.pill--active]="active">
      <ng-content />
      <button type="button" (click)="toggle.emit(!active)">×</button>
    </span>
  `,
  styles: [`
    .pill { display: inline-flex; align-items: center; gap: 0.25rem; padding: 0.25rem 0.5rem; border-radius: 9999px; background: #e0f2fe; }
    .pill--active { background: #1d4ed8; color: #fff; }
    button { all: unset; cursor: pointer; font-size: 0.75rem; }
  `]
})
export class PillComponent {
  @Input({ required: true }) active!: boolean;
  @Output() toggle = new EventEmitter<boolean>();
}

@Component({
  selector: 'app-pill-demo',
  standalone: true,
  imports: [CommonModule, PillComponent],
  template: `
    <app-pill [active]="selected" (toggle)="selected = $event">
      Component Directive
    </app-pill>
    <p>状態: {{ selected ? 'ON' : 'OFF' }}</p>
  `
})
export class PillDemoComponent {
  protected selected = false;
}
```

## ベストプラクティス
- standalone指定でモジュール依存を減らし、利用側は`imports`に追加するだけで使えるようにする
- Input/Outputは必須フラグと型定義で契約を明示し、ステートレス設計を維持する
- `ng-content`で柔軟なコンテンツ挿入を許可しつつ、スタイルはコンポーネント内で閉じる

## 注意点
- ビジネスロジックはサービスへ委譲し、UI表現に集中させる
- 過度なスタイルやサイズ依存を避け、利用側がカスタマイズできる余地を残す
- ChangeDetection戦略を必要に応じて`OnPush`へ切り替え、再描画コストを抑える

## 関連技術
- Standalone Components
- Angular Signals
- ChangeDetectorRef
