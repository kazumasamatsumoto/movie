# #545 「PipeTransform インターフェース」

## 概要
`PipeTransform`インターフェースはカスタムPipeが実装するインターフェースで、`transform`メソッドを定義し値の変換処理を行う。

## 学習目標
- PipeTransformインターフェースの役割を理解する
- `transform`メソッドのシグネチャと型注釈を学ぶ
- Pipeクラスに実装する際のベストプラクティスを把握する

## 技術ポイント
- `export class MyPipe implements PipeTransform`
- `transform(value: T, ...args: any[]): R`
- 型パラメータで入出力を限定し型安全性を高める

## 📺 画面表示用コード（動画用）
```typescript
export class TruncatePipe implements PipeTransform {
  transform(value: string, limit = 20): string { ... }
}
```

## 💻 詳細実装例（学習用）
```typescript
export class JsonParsePipe implements PipeTransform {
  transform(value: string): unknown {
    try {
      return JSON.parse(value);
    } catch {
      return null;
    }
  }
}
```

## ベストプラクティス
- 入力と出力の型を明示し、コンポーネント側で補完が効くようにする
- 可変長引数を利用する場合はrestパラメータで定義
- 例外処理や入力チェックを行い安全に変換

## 注意点
- PipeTransformを実装しないとコンパイル時に警告が出る
- `transform`が純粋関数でないと予期しない副作用が起きる
- 引数の型をanyにすると型安全性が失われる

## 関連技術
- PipeTransform
- TypeScript型注釈
- カスタムPipe実装
