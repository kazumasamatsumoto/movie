# #067 ngDoCheck - 変更検知のカスタマイズ

## 概要
Angular v20におけるngDoCheckの使用方法を学びます。Angularの変更検知をカスタマイズし、オブジェクトの深い変更やカスタムロジックによる変更検知を行う方法について解説します。

## 学習目標
- ngDoCheckの基本的な使用方法を理解する
- 変更検知のカスタマイズ方法を習得する
- パフォーマンスを考慮した実装方法を身につける

## 📺 画面表示用コード

```typescript
// ngDoCheckの基本実装
export class CustomChangeDetectionComponent implements DoCheck {
  @Input() data: any;
  private previousData: any;
  
  ngDoCheck() {
    if (this.data !== this.previousData) {
      console.log('データが変更されました');
      this.previousData = this.data;
    }
  }
}
```

```typescript
// 深いオブジェクトの変更検知
export class DeepObjectComponent implements DoCheck {
  @Input() user: User = {};
  private previousUser: User = {};
  
  ngDoCheck() {
    if (this.hasUserChanged(this.user, this.previousUser)) {
      this.onUserChange();
      this.previousUser = { ...this.user };
    }
  }
}
```

## 技術ポイント

### 1. ngDoCheckの基本
ngDoCheckは、Angularの変更検知サイクルで呼び出されるHookです。DoCheckインターフェースを実装することで使用できます。

### 2. 変更検知のカスタマイズ
- オブジェクトの深い変更の検知
- カスタムロジックによる変更検知
- パフォーマンスの最適化

### 3. パフォーマンス考慮
- 頻繁に実行されるため軽量な処理を心がける
- 不要な変更検知を避ける
- 効率的な比較アルゴリズムの使用

## 実践的な活用例

### 1. オブジェクトの深い変更検知
```typescript
export class ObjectChangeComponent implements DoCheck {
  @Input() config: Config = {};
  private previousConfig: Config = {};
  
  ngDoCheck() {
    if (this.hasConfigChanged()) {
      this.updateConfiguration();
      this.previousConfig = JSON.parse(JSON.stringify(this.config));
    }
  }
  
  private hasConfigChanged(): boolean {
    return JSON.stringify(this.config) !== JSON.stringify(this.previousConfig);
  }
}
```

### 2. 配列の変更検知
```typescript
export class ArrayChangeComponent implements DoCheck {
  @Input() items: Item[] = [];
  private previousItems: Item[] = [];
  
  ngDoCheck() {
    if (this.hasItemsChanged()) {
      this.updateItems();
      this.previousItems = [...this.items];
    }
  }
  
  private hasItemsChanged(): boolean {
    if (this.items.length !== this.previousItems.length) {
      return true;
    }
    return this.items.some((item, index) => 
      item.id !== this.previousItems[index]?.id
    );
  }
}
```

## ベストプラクティス

1. **軽量な処理**: 頻繁に実行されるため軽量な処理を心がける
2. **効率的な比較**: 不要な変更検知を避ける
3. **パフォーマンス監視**: パフォーマンスへの影響を監視
4. **適切な使用**: 必要な場合のみ使用する

## 注意点

- 頻繁に実行されるためパフォーマンスに注意
- 無限ループの回避
- 重い処理は避ける
- 適切な変更検知ロジックの実装

## 関連技術
- 変更検知
- パフォーマンス最適化
- オブジェクト比較
- Angular v20のSignal
