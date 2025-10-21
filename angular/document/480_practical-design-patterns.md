# #480 「実用 Directive の設計パターン」

## 概要
実用的なディレクティブはイベント監視・状態管理・Input/Outputによるカスタマイズを組み合わせ、再利用性と拡張性を両立する。ObserverやHostBindingなど共通のパターンを押さえることが重要。

## 学習目標
- 実用ディレクティブに共通する設計パターンを理解する
- Input/Output、HostListener/HostBinding、Observerの組み合わせを学ぶ
- サービス抽象化やドキュメント整備など品質向上のポイントを把握する

## 技術ポイント
- Observerパターン（IntersectionObserver、ResizeObserver、MutationObserver）
- Input/Outputで柔軟性を確保、HostBindingで視覚的状態を反映
- Renderer2でDOM操作、DestroyRefで副作用管理

## 📺 画面表示用コード（動画用）
```markdown
- Observer + Output通知
- HostListener + HostBinding
- Inputオプション + デフォルト値
```

## 💻 詳細実装例（学習用）
```markdown
1. Input/Output設計  
   - `@Input() options: TooltipOptions`  
   - `@Output() closed = new EventEmitter<void>()`

2. Observer活用  
   - IntersectionObserverで可視領域を監視  
   - ResizeObserverで要素サイズ変化に対応

3. UI反映  
   - HostBindingでクラスやスタイルを更新  
   - Renderer2で必要なDOM要素を生成

4. 副作用管理  
   - DestroyRefやngOnDestroyで監視解除  
   - サービス経由で共有状態を管理

5. ドキュメント・テスト  
   - README/StorybookでAPIを共有  
   - TestBedでホストコンポーネントを使い挙動を検証
```

## ベストプラクティス
- パターンをテンプレート化し新しいディレクティブ開発を高速化
- Inputで設定、Outputで通知、HostBindingで状態、Observerでイベントという構造を意識
- テスト・ドキュメント・デザインシステムと連携し保守性を高める

## 注意点
- パターン化しすぎると特定要件に合わない場合があるため柔軟さも確保
- Observerはブラウザ依存があるためPolyfillやFallbackを検討
- カスタマイズ性が高い場合は破壊的変更が発生しないようバージョニング管理

## 関連技術
- IntersectionObserver / ResizeObserver
- HostListener / HostBinding
- Angular Style Guide / Storybook
