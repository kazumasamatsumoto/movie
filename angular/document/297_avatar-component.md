# #297 「Avatar Component - アバター表示」

## 概要
Avatar Componentはユーザーのプロフィール画像やイニシャルを表示し、サイズ・形状・フォールバックを統一したUIとして提供する。

## 学習目標
- 画像とイニシャルのフォールバックを実装する
- サイズと形状をInputで切り替える
- alt/aria属性でアクセシビリティを確保する

## 技術ポイント
- Errorイベントでフォールバック
- CSS変数でサイズ制御
- aria-label

## 📺 画面表示用コード（動画用）
```typescript
@Component({ selector: 'app-avatar', standalone: true, template: `<figure class="avatar" [class.avatar--rounded]="shape==='rounded'" [style.--avatar-size.px]="size"><ng-container *ngIf="!broken && src; else fallback"><img [src]="src" [alt]="alt" (error)="onError()"></ng-container><ng-template #fallback><span aria-hidden="true">{{ initials }}</span></ng-template></figure>`, changeDetection: ChangeDetectionStrategy.OnPush })
export class AvatarComponent {
  @Input() src?: string;
  @Input() alt = '';
  @Input() initials = '?';
  @Input() size = 40;
  @Input() shape: 'circle' | 'rounded' = 'circle';
  broken = false;
  onError(): void { this.broken = true; }
}
```

```css
.avatar { --avatar-size: 40px; width: var(--avatar-size); height: var(--avatar-size); border-radius: 50%; overflow: hidden; background: #e2e8f0; color: #1e293b; display: inline-flex; align-items: center; justify-content: center; font-weight: 600; }
.avatar--rounded { border-radius: 12px; }
.avatar img { width: 100%; height: 100%; object-fit: cover; }
```

```html
<app-avatar src="/assets/user.png" alt="山田太郎" initials="YT" [size]="48"></app-avatar>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-avatar-demo',
  standalone: true,
  imports: [AvatarComponent],
  template: `
    <app-avatar src="/assets/users/miku.png" alt="初音ミク" initials="MI" [size]="56"></app-avatar>
    <app-avatar initials="AK" shape="rounded" [size]="40"></app-avatar>
    <app-avatar src="/broken/url.png" alt="ロード失敗" initials="??" [size]="32"></app-avatar>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class AvatarDemoComponent {}
```

## ベストプラクティス
- イニシャルの生成はユーティリティ化し、ローマ字や多言語に対応する
- altを適切に設定し、装飾目的の場合はaria-hiddenをtrueにする
- 画像キャッシュを考慮して`loading="lazy"`を付与する

## 注意点
- 透過背景の画像は背景色とコントラストを確認する
- 高解像度ディスプレイ向けに`srcset`を用意する
- サイズ変更時はタイポグラフィに合わせてフォントサイズを調整する

## 関連技術
- Accessibility
- CSS変数
- Lazy Loading
