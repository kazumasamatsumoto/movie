# #439 「Directive のベストプラクティス」

## 概要
ディレクティブのベストプラクティスは単一責務、プラットフォーム非依存、テスト/ドキュメント整備を中心に、保守性と再利用性を高める指針である。

## 学習目標
- 主要なベストプラクティスを体系的に理解する
- DOM操作や副作用管理の安全策を学ぶ
- テストとドキュメントの重要性を認識する

## 技術ポイント
- Renderer2/HostBindingを活用し直接DOMアクセスを避ける
- DestroyRefやngOnDestroyで副作用を確実に解除
- Input/Outputを明確に定義

## 📺 画面表示用コード（動画用）
```typescript
@HostBinding('class.is-active') active = false;
@HostListener('click') toggle(): void { this.active = !this.active; }
```

## 💻 詳細実装例（学習用）
```markdown
- 単一責務: 見た目変更だけに集中しビジネスロジックはサービスへ
- プラットフォーム非依存: Renderer2/PLATFORM_IDでガード
- テスト: ホストコンポーネントを使い挙動を検証
- ドキュメント: 目的・API・使用例を整備
```

## ベストプラクティス
- セレクタ命名・プレフィックス統一で衝突を防ぐ
- SignalsやComputedで状態更新を最小化
- イベント/リスナーは必ずクリーンアップ

## 注意点
- 1つのディレクティブで複雑な機能を詰め込まない
- DOM操作の乱用はパフォーマンスと移植性を損なう
- メンテナンス性のためドキュメントとテストを欠かさない

## 関連技術
- Renderer2
- DestroyRef
- Angular Style Guide
