# #435 「Directive のデバッグ」

## 概要
ディレクティブのデバッグではログ出力、Angular DevTools、テストによる再現を組み合わせ、適用漏れやイベント未発火を特定する。

## 学習目標
- デバッグ方法の選択肢を理解する
- `ngDevMode`や`console`を使った軽量な検証手法を学ぶ
- DevToolsでディレクティブの状態を確認する方法を把握する

## 技術ポイント
- `if (ngDevMode) console.debug(...)`
- Angular DevToolsでDirectiveタブを確認
- テストで再現シナリオを用意しリグレッションを防ぐ

## 📺 画面表示用コード（動画用）
```typescript
if (ngDevMode) console.debug('active', this.isActive);
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appDebug]',
  standalone: true
})
export class DebugDirective {
  @HostBinding('class.is-debug') debug = false;

  @HostListener('click')
  onClick(): void {
    this.debug = !this.debug;
    if (ngDevMode) {
      console.debug('[appDebug] toggled', this.debug);
    }
  }
}
```

## ベストプラクティス
- デバッグログは`ngDevMode`で囲み、本番バンドルから除外
- 開発中はAngular DevToolsのElementsタブでディレクティブ適用状況を確認
- テストにデバッグ観点を落とし込んで長期的に再現性を確保

## 注意点
- 過剰なログはパフォーマンス悪化や情報漏洩につながるため最小限に
- SSR環境ではconsoleが存在しない場合があるのでガードを入れる
- デバッグ用クラスや属性を出荷前に削除しておく

## 関連技術
- Angular DevTools
- Testing Library
- ngDevMode
