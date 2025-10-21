# #505 「スケルトン表示」

## 概要
スケルトン表示は読み込み中のプレースホルダーとして使用され、構造ディレクティブのelseテンプレートで提供することで簡単に差し替えられる。

## 学習目標
- スケルトンテンプレートの設計と適用方法を理解する
- Skeletonテンプレートを`ng-template`で渡す手順を学ぶ
- アニメーションやテーマと連携する方法を把握する

## 技術ポイント
- `*appLoadingIf="loading; else skeleton"`
- Skeletonテンプレートでシマーアニメーションを定義
- Contextでloading/errorを渡し条件に応じて表示

## 📺 画面表示用コード（動画用）
```html
<ng-template #skeleton>
  <div class="skeleton skeleton-title"></div>
  <div class="skeleton skeleton-body"></div>
></ng-template>
```

## 💻 詳細実装例（学習用）
```html
<article *appLoadingIf="loading; else skeleton">
  <h2>{{ data.title }}</h2>
  <p>{{ data.body }}</p>
</article>

<ng-template #skeleton>
  <div class="skeleton skeleton-title shimmer"></div>
  <div class="skeleton skeleton-body shimmer"></div>
</ng-template>
```

CSS例:
```css
.skeleton { background: #e2e8f0; border-radius: 0.5rem; margin-bottom: 0.75rem; }
.shimmer { animation: shimmer 1.5s infinite; }
@keyframes shimmer { 0% { opacity: .45; } 50% { opacity: .9; } 100% { opacity: .45; } }
```

## ベストプラクティス
- Skeletonテンプレートを再利用できるよう共通ng-templateやコンポーネントを用意
- シマーアニメーションで読み込み感を演出
- ダークテーマなどに合わせ色を調整

## 注意点
- Skeletonが過剰に点滅しないようアニメーション速度を適切に調整
- 内容量に応じてSkeletonの形状を変える
- SSRではSkeletonだけがレンダリングされる可能性があるため注意

## 関連技術
- LoadingIf Directive
- CSSアニメーション
- Design Systemのスケルトンコンポーネント
