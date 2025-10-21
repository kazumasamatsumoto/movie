# #254 「Presentation Component - 表示専用」

## 概要
Presentation ComponentはUIの描画専用に設計された軽量コンポーネントで、状態管理や副作用を持たず親コンポーネントから受け取ったデータを視覚化する。

## 学習目標
- Presentation Componentの責務範囲を理解する
- InputとOutputでシンプルな契約を定義する
- OnPush戦略とスタイルの内製化で表示専用を実現する

## 技術ポイント
- Standalone Componentでの軽量定義
- ChangeDetectionStrategy.OnPush
- Template入力の型定義

## 📺 画面表示用コード（動画用）
```typescript
@Component({
  selector: 'app-profile-card',
  standalone: true,
  template: `<article><h3>{{ vm.name }}</h3><p>{{ vm.role }}</p></article>`,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class ProfileCardComponent {
  @Input({ required: true }) vm!: Readonly<ProfileVm>;
}
```

```typescript
export type ProfileVm = {
  readonly name: string;
  readonly role: string;
  readonly avatarUrl?: string;
};
```

```typescript
@Component({
  selector: 'app-profile-card-actions',
  standalone: true,
  template: `<button (click)="invite.emit(vm.email)">招待</button>`,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class ProfileCardActionsComponent {
  @Input({ required: true }) vm!: Readonly<ProfileVm & { email: string }>;
  @Output() invite = new EventEmitter<string>();
}
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-profile-card-shell',
  standalone: true,
  imports: [ProfileCardComponent, ProfileCardActionsComponent],
  template: `
    <app-profile-card [vm]="vm"></app-profile-card>
    <app-profile-card-actions [vm]="vm" (invite)="onInvite($event)"></app-profile-card-actions>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class ProfileCardShellComponent {
  @Input({ required: true }) vm!: Readonly<ProfileVm & { email: string }>;
  @Output() invited = new EventEmitter<string>();

  onInvite(email: string): void {
    this.invited.emit(email);
  }
}
```

## ベストプラクティス
- 見た目に関するロジックのみを内部に保持し、ビジネスロジックは親へ委譲する
- ViewModel型を決めてInputに適用し、テンプレートでの補完を効かせる
- Outputイベントには副作用を含めず親コンポーネントに任せる

## 注意点
- Presentation Componentにサービス注入を行わない
- Inputに可変オブジェクトを渡す場合は参照が変わるように更新する
- UI表示のバリエーションはng-contentや別コンポーネントで扱う

## 関連技術
- Smart/Containerパターン
- Angular Signals
- Storybookドキュメンテーション
