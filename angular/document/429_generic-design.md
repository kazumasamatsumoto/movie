# #429 「汎用的な設計」

## 概要
汎用設計は単一責務と拡張ポイントを兼ね備え、ジェネリクスやStrategyパターンを活用して様々なケースに適応できるディレクティブを目指す。

## 学習目標
- 汎用化のための設計原則を理解する
- StrategyやDIによる拡張点の設計方法を学ぶ
- 型パラメータを利用した柔軟なAPIを把握する

## 技術ポイント
- InputでStrategyオブジェクトや関数を受け取る
- Dependency Injectionで抽象サービスを注入
- GenericsでInputの型制約を柔軟にする

## 📺 画面表示用コード（動画用）
```typescript
@Input() appValidator!: (value: string) => boolean;
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appValidator]',
  standalone: true
})
export class ValidatorDirective {
  @Input() appValidator?: (value: string) => boolean;
  @Output() validation = new EventEmitter<boolean>();

  @HostListener('input', ['$event.target.value'])
  onInput(value: string): void {
    const fn = this.appValidator ?? ((v: string) => v.length > 0);
    this.validation.emit(fn(value));
  }
}
```

## ベストプラクティス
- StrategyやCallbackをInputで受け取り、利用側が自由に挙動を差し替えられるようにする
- 型パラメータを活用して複数種類のデータを扱えるようにする
- 仕様変更に強いようドキュメントとテストを充実させる

## 注意点
- 汎用化しすぎると使い方が難解になるため、デフォルト挙動を明確にする
- 依存関係が増えすぎると設定が煩雑化するのでバランスを取る
- Strategyを渡さない場合のフォールバック実装を忘れない

## 関連技術
- Strategyパターン
- Generics
- Dependency Injection
