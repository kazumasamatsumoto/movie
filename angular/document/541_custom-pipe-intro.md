# #541 「カスタム Pipe の作成」

## 概要
カスタムPipeはテンプレートで繰り返し行うデータ整形を再利用可能な変換としてまとめる仕組みで、独自の`transform`ロジックを定義できる。

## 学習目標
- カスタムPipe作成の手順を理解する
- transformメソッドに純粋な変換処理を書く重要性を学ぶ
- Standalone Pipeとして簡単に利用できる設定を把握する

## 技術ポイント
- `@Pipe({ name: 'myPipe', standalone: true })`
- `class MyPipe implements PipeTransform { transform(value: T, ...args: any[]): R }`
- `ng g pipe`で雛形生成

## 📺 画面表示用コード（動画用）
```bash
ng g pipe shared/truncate --standalone
```

## 💻 詳細実装例（学習用）
```typescript
@Pipe({
  name: 'truncate',
  standalone: true
})
export class TruncatePipe implements PipeTransform {
  transform(value: string, limit = 20, suffix = '...'): string {
    if (!value || value.length <= limit) return value;
    return `${value.substring(0, limit)}${suffix}`;
  }
}
```

## ベストプラクティス
- 純粋関数として実装し副作用を避ける
- 元のデータを変更せず表示のみを変換
- 引数にデフォルト値を設定し使いやすくする

## 注意点
- カスタムPipeはCommonModuleに自動登録されないためstandaloneを推奨
- 重い処理はパフォーマンスへ影響するので注意
- 非純粋Pipeにすると毎回再計算される点に留意

## 関連技術
- PipeTransform
- Standalone Pipe
- カスタムPipeテスト
