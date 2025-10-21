# #607 「ReactiveFormsModule のインポート」

## 概要
リアクティブフォームを有効にするにはReactiveFormsModuleをインポートし、コンポーネントやモジュールで利用できるよう登録する。

## 学習目標
- ReactiveFormsModuleの役割を理解する
- スタンドアロンとNgModuleでの設定方法を把握する
- 追加されるディレクティブとサービスを把握する

## 技術ポイント
- ReactiveFormsModuleをimportsに追加するとformGroup系ディレクティブが利用可能
- FormBuilderなどのサービスも同モジュールで提供
- 共通モジュール化して複数画面で再利用できる

## 📺 画面表示用コード（動画用）
```typescript
import { ReactiveFormsModule } from '@angular/forms';
```

```typescript
@Component({
  standalone: true,
  imports: [ReactiveFormsModule]
})
```

## 💻 詳細実装例（学習用）
```typescript
@NgModule({
  imports: [CommonModule, ReactiveFormsModule],
  exports: [ReactiveFormsModule]
})
export class SharedReactiveModule {}
```

## ベストプラクティス
- リアクティブフォーム用の共有モジュールを準備して重複を減らす
- FormBuilderを活用しテスト可能なコードスタイルを徹底する
- Featureモジュールで必要なモジュールのみ読み込む

## 注意点
- ReactiveFormsModuleの追加を忘れるとformGroupディレクティブが無効
- テンプレート駆動と両方読み込む場合は目的を明確にする
- SSR環境では不要なサービスを読み込まないよう調整する

## 関連技術
- ReactiveFormsModule
- FormBuilder
- モジュール設計
