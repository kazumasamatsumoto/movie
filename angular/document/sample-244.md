# #244 「動的 Component のデバッグ」

## 概要
動的に生成したコンポーネントが期待通りに表示されない場合のデバッグ手法を整理し、ログ・DevTools・Angular DevToolsを活用して原因を特定します。

## 学習目標
- createComponentの呼び出しや入力設定のタイミングを確認する方法を理解する
- DevToolsで実際に生成されたDOMを確認し、ビューが挿入されているかを検証する
- Change DetectionやInjector問題など典型的なトラブルシューティングを習得する

## 技術ポイント
- **ログ出力**: `console.debug`で生成/破棄のタイミングを記録
- **DOM検証**: ブラウザDevToolsで`ng-container`の展開結果を確認
- **Angular DevTools**: Componentツリーで動的生成したコンポーネントの存在を確認

## 📺 画面表示用コード（動画用）

```typescript
const ref = this.host.createComponent(MyComponent);
console.debug('component created', ref);
```

```typescript
ref.instance.config = config;
ref.changeDetectorRef.detectChanges();
```

```typescript
console.debug('destroy called');
ref.destroy();
```

## 💻 詳細実装例（学習用）
```markdown
### デバッグチェックリスト
1. `createComponent`が呼ばれているかログで確認
2. `ComponentRef`がundefinedになっていないか確認
3. Input設定後に`detectChanges()`を呼んでいるか
4. DevToolsでDOMにコンポーネントが生成されているか確認
5. Angular DevToolsでコンポーネントツリーに表示されているか確認
6. Injectorやプロバイダーが正しく渡っているかをコンソールで`ref.injector.get(...)`して検証
```

## ベストプラクティス
- 生成処理をラップしたサービスにログを入れ、動的生成の流れを追跡できるようにする
- コンポーネント側にデバッグ用Input（例：`debugId`）を用意し、どのコンポーネントが表示されているか識別しやすくする
- Angular DevToolsを利用して動的コンポーネントがChange Detectionに参加しているか確認する

## 注意点
- `detectChanges()`を呼び忘れると、描画されない（データバインディングが更新されない）ことがある
- Injector不足で依存サービスが見つからない場合、エラーが遅延して表示されないことがあるのでログで補足する
- destroy後も参照が残っていると再生成時に混乱するため、状態をリセットする

## 関連技術
- 動的コンポーネントのテスト（#243）
- ComponentRef / ViewContainerRef（#232, #222）
- Angular DevToolsとブラウザDevToolsの活用
