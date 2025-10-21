# #479 「ナビゲーションのアクティブ化」

## 概要
ScrollSpyと連携して現在表示中のセクションIDを受け取り、ナビゲーションリンクにアクティブクラスを付与してユーザーに位置を示す。

## 学習目標
- ScrollSpyからのイベントを受け取りナビゲーションを更新する方法を理解する
- アクティブクラスの付与とハッシュ更新を学ぶ
- スムーズスクロール等との連携を把握する

## 技術ポイント
- Outputイベントで受け取ったIDとナビリンクを照合
- HostBindingまたはngClassでアクティブ状態を表示
- ハッシュ更新に`Location.replaceState`などを利用

## 📺 画面表示用コード（動画用）
```html
<nav [appScrollSpy]="sections" (sectionChange)="active = $event">
  <a [class.is-active]="active === 'section-1'" href="#section-1">Section 1</a>
</nav>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-scrollspy-nav',
  standalone: true,
  imports: [CommonModule, ScrollSpyDirective],
  template: `
    <nav appScrollSpy [spyTargets]="sections" (sectionChange)="setActive($event)">
      <a *ngFor="let section of sections" [class.is-active]="active === section.id" [href]="'#' + section.id">
        {{ section.label }}
      </a>
    </nav>
  `
})
export class ScrollSpyNavComponent implements AfterViewInit {
  protected sections = [
    { id: 'section-1', label: '概要' },
    { id: 'section-2', label: '詳細' },
    { id: 'section-3', label: '例' }
  ];
  protected active = this.sections[0].id;

  constructor(private readonly location: Location) {}

  protected setActive(id: string): void {
    this.active = id;
    this.location.replaceState(`#${id}`);
  }
}
```

## ベストプラクティス
- ナビゲーションのアクティブ状態はクラスで表現し、CSSで視覚化
- ハッシュを更新してページ再読み込み時も同じ位置に戻れるようにする
- SSG/SSR環境ではハッシュ更新がブラウザ側で行われる点に留意

## 注意点
- `replaceState`はブラウザ履歴にエントリーを追加しないため適切に使用
- スクロール位置が不正確な場合はセクションへのオフセットを調整
- ナビゲーションリンクがクリックされた際にはスムーズスクロールを実装するとUXが向上

## 関連技術
- ScrollSpyDirective
- Router fragment
- Smooth Scroll API
