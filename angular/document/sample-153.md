# #153 「テンプレート参照変数のスコープ」

## 概要
Angular v20におけるテンプレート参照変数のスコープルール。定義されたテンプレート内でのみ有効な参照の仕組みを理解し、適切なスコープ設計で予測可能なコードを実現する方法を学ぶ。

## 学習目標
- テンプレート参照変数のスコープを理解する
- スコープルールを学ぶ
- 適切な参照設計を把握する

## 技術ポイント
- 同一テンプレート内での参照
- 異なるテンプレート間の制限
- スコープの境界
- 適切な参照設計

## 📺 画面表示用コード

### 同一テンプレート内での参照
```typescript
@Component({
  selector: 'app-same-scope',
  template: `
    <div #container class="container">
      <div #item1>項目1</div>
      <div #item2>項目2</div>
      <button (click)="item1.style.color = 'red'">項目1を赤に</button>
      <button (click)="item2.style.color = 'blue'">項目2を青に</button>
    </div>
  `
})
export class SameScopeComponent {}
```

### スコープ外での参照（エラー例）
```typescript
@Component({
  selector: 'app-scope-error',
  template: `
    <div #outer>外側要素</div>
    <ng-container>
      <div #inner>内側要素</div>
      <!-- これはエラー: outerは異なるスコープ -->
      <button (click)="outer.style.display = 'none'">エラー</button>
    </ng-container>
  `
})
export class ScopeErrorComponent {}
```

## 実践的な活用例
- 適切なスコープ設計
- 参照の可視性管理
- テンプレート構造の最適化

## ベストプラクティス
- 明確なスコープ境界
- 適切な参照配置
- 予測可能な設計

## 注意点
- スコープ外参照の回避
- テンプレート構造の考慮
- デバッグのしやすさ

## 関連技術
- テンプレート構造
- スコープ管理
- 参照設計
