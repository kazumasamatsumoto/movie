# #273 「KISS 原則の適用」

## 概要
KISS（Keep It Simple, Stupid）原則は、過度な複雑さを避け最も単純な構造で実装することで、理解しやすいコンポーネントを目指す指針である。

## 学習目標
- コンポーネントの複雑化を抑える判断軸を学ぶ
- Template制御構文で分岐をシンプルに表現する
- テストシナリオを最小限に保つ設計を身につける

## 技術ポイント
- Control Flow構文（@if/@switch）
- 単純なViewModelとOnPush
- シンプルなInput契約

## 📺 画面表示用コード（動画用）
```typescript
@Component({ selector: 'app-status-label', standalone: true, template: `@switch (status) { @case ('active') { <span class="ok">稼働中</span> } @case ('paused') { <span class="warn">一時停止</span> } @default { <span class="muted">不明</span> } }` })
export class StatusLabelComponent {
  @Input({ required: true }) status: 'active' | 'paused' | 'unknown' = 'unknown';
}
```

```typescript
export type StatusVm = {
  readonly status: 'active' | 'paused' | 'unknown';
};
```

```typescript
@Component({
  selector: 'app-status-card',
  standalone: true,
  imports: [StatusLabelComponent],
  template: `<article><h3>{{ title }}</h3><app-status-label [status]="status"></app-status-label></article>`
})
export class StatusCardComponent {
  @Input({ required: true }) title = '';
  @Input({ required: true }) status: StatusVm['status'] = 'unknown';
}
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-status-dashboard',
  standalone: true,
  imports: [StatusCardComponent],
  template: `
    <app-status-card title="配信サーバー" [status]="servers()"></app-status-card>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class StatusDashboardComponent {
  private readonly status = signal<StatusVm['status']>('unknown');
  readonly servers = this.status.asReadonly();

  setStatus(value: StatusVm['status']): void {
    this.status.set(value);
  }
}
```

## ベストプラクティス
- 分岐はControl Flow構文で表現し、複雑なロジックは避ける
- Inputは必要最低限の値に限定し設定を増やさない
- テストケースを2〜3件に抑えられる設計を意識する

## 注意点
- 条件が増え始めたら別コンポーネント化を検討する
- Templateが読みにくくなったら再構成する
- シンプルさを保つために機能追加時の影響を評価する

## 関連技術
- Angular Control Flow
- Signals
- シンプルなViewModel設計
