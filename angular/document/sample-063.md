# #063 ngOnChanges - SimpleChanges の活用

## 概要
Angular v20におけるSimpleChangesオブジェクトの詳細な活用方法を学びます。変更の詳細情報を効率的に取得し、適切な処理を実行する方法について解説します。

## 学習目標
- SimpleChangesオブジェクトの詳細を理解する
- 変更前後の値の比較方法を習得する
- 効率的な変更処理の実装方法を身につける

## 📺 画面表示用コード

```typescript
// SimpleChangesの詳細活用
export class AdvancedChangeComponent implements OnChanges {
  @Input() user: User = { id: '', name: '' };
  @Input() settings: Settings = { theme: 'light' };
  
  ngOnChanges(changes: SimpleChanges) {
    if (changes['user']) {
      const change = changes['user'];
      console.log('変更前:', change.previousValue);
      console.log('変更後:', change.currentValue);
      console.log('初回変更:', change.firstChange);
    }
  }
}
```

```typescript
// 条件付き処理
ngOnChanges(changes: SimpleChanges) {
  if (changes['user'] && !changes['user'].firstChange) {
    this.onUserChange(changes['user'].currentValue);
  }
}
```

## 技術ポイント

### 1. SimpleChangesオブジェクトの詳細
SimpleChangesは、各プロパティの変更情報を含むオブジェクトです：
- `previousValue`: 変更前の値
- `currentValue`: 変更後の値  
- `firstChange`: 初回変更かどうかのboolean値

### 2. 変更検知の最適化
効率的な変更処理のためのパターン：
- 特定プロパティのみの監視
- 初回変更の除外
- 値の比較による条件分岐

### 3. Angular v20での改善
- より効率的な変更検知
- Signalベースのリアクティブシステムとの統合
- パフォーマンスの向上

## 実践的な活用例

### 1. 値の比較による条件分岐
```typescript
export class ComparisonComponent implements OnChanges {
  @Input() count: number = 0;
  
  ngOnChanges(changes: SimpleChanges) {
    if (changes['count']) {
      const change = changes['count'];
      if (change.previousValue < change.currentValue) {
        this.onCountIncrease();
      } else if (change.previousValue > change.currentValue) {
        this.onCountDecrease();
      }
    }
  }
}
```

### 2. 複雑なオブジェクトの変更監視
```typescript
export class ObjectChangeComponent implements OnChanges {
  @Input() config: Config = {};
  
  ngOnChanges(changes: SimpleChanges) {
    if (changes['config'] && !changes['config'].firstChange) {
      const oldConfig = changes['config'].previousValue;
      const newConfig = changes['config'].currentValue;
      
      if (oldConfig.theme !== newConfig.theme) {
        this.updateTheme(newConfig.theme);
      }
      
      if (oldConfig.language !== newConfig.language) {
        this.updateLanguage(newConfig.language);
      }
    }
  }
}
```

### 3. 配列の変更監視
```typescript
export class ArrayChangeComponent implements OnChanges {
  @Input() items: string[] = [];
  
  ngOnChanges(changes: SimpleChanges) {
    if (changes['items'] && !changes['items'].firstChange) {
      const oldItems = changes['items'].previousValue || [];
      const newItems = changes['items'].currentValue || [];
      
      if (newItems.length > oldItems.length) {
        this.onItemsAdded(newItems.slice(oldItems.length));
      } else if (newItems.length < oldItems.length) {
        this.onItemsRemoved();
      }
    }
  }
}
```

## ベストプラクティス

1. **効率的な比較**: 必要な時のみ値の比較を実行
2. **初回変更の考慮**: firstChangeフラグを適切に活用
3. **パフォーマンス**: 重い処理は避け、軽量な処理を心がける
4. **エラーハンドリング**: 変更処理での例外処理

## 注意点

- 初回変更（firstChange = true）の適切な処理
- パフォーマンスへの影響を考慮
- 深いオブジェクトの変更検知の制限
- 無限ループの回避

## 関連技術
- ngOnChanges
- 変更検知
- Angular v20のSignal
- パフォーマンス最適化
