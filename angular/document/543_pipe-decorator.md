# #543 「@Pipe デコレータ」

## 概要
@PipeデコレータはカスタムPipeのメタデータを定義し、テンプレートで使用する名前や純粋/非純粋の設定を行う。

## 学習目標
- @Pipeデコレータの役割を理解する
- name/pure/standaloneプロパティの意味を学ぶ
- Pipeクラスとデコレータの関係を把握する

## 技術ポイント
- `@Pipe({ name: 'truncate', standalone: true, pure: true })`
- nameはテンプレートでの使用名
- pureで再計算タイミングを制御

## 📺 画面表示用コード（動画用）
```typescript
@Pipe({ name: 'truncate', standalone: true })
export class TruncatePipe implements PipeTransform { ... }
```

## 💻 詳細実装例（学習用）
```typescript
@Pipe({
  name: 'filter',
  standalone: true,
  pure: false
})
export class FilterPipe implements PipeTransform {
  transform<T>(list: T[], predicate: (item: T) => boolean): T[] {
    return list.filter(predicate);
  }
}
```

## ベストプラクティス
- Pipeは小文字+プレフィックスで衝突を避ける
- pureは基本true、可変データ処理が必要な場合のみfalse
- Standalone指定でモジュール依存を減らす

## 注意点
- pure: falseにするとパフォーマンスへ影響
- nameは一意にする
- デコレータを忘れるとPipeとして認識されない

## 関連技術
- PipeTransform
- Standalone API
- 純粋/非純粋Pipe
