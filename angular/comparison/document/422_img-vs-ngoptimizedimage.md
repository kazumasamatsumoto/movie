# #422 「<img> vs NgOptimizedImage あなたはどっち派？」

## 概要
素のimgは自由だが最適化を自分で管理する必要がある。NgOptimizedImageはAngularがレスポンシブ・遅延読み込み設定を肩代わりする。

## 学習目標
- 素の<img>の構成と得意なシナリオを整理する
- NgOptimizedImageの採用メリットを理解する
- プロジェクト条件に応じた使い分け基準を決める

## 技術ポイント
- 素の<img>を成り立たせる主要API/構成要素
- NgOptimizedImageで押さえる設定やコード記述
- 両者を共存・移行させるためのブリッジ手法

## 📺 画面表示用コード（動画用）
**素のimg：自己責任で最適化**
```typescript
<img src="/assets/hero.jpg" alt="hero" />
```

**NgOptimizedImage：最適化込み**
```typescript
<img
  ngOptimizedImage
  [src]="hero.photo"
  width="320"
  height="200"
  priority
  alt="hero"
/>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-hero-card',
  standalone: true,
  imports: [NgOptimizedImage],
  templateUrl: './hero-card.component.html',
})
export class HeroCardComponent {
  @Input() hero!: Hero;
}
```

## ベストプラクティス
- LCP候補の画像は`priority`を付け、その他は`loading='lazy'`や`ngSrcset`でレスポンシブにする
- CMS等で画像URLを生成するなら`ngSrc`を使い、ビルド時検証を有効化する
- 素のimgを使う場合も必ずwidth/heightを指定しCLSを避ける

## 注意点
- NgOptimizedImageはAngular v15+が必要で、SSRとの組み合わせも検証する
- priorityを多用すると帯域を圧迫するので1ページ1〜2枚に制限する
- 外部CDNのURLを使う際はCORS設定を確認する

## 関連技術
- NgOptimizedImage
- 画像最適化
- Core Web Vitals
