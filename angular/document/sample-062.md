# #062 ngOnChanges - 入力プロパティ変更時

## 概要
Angular v20におけるngOnChangesの使用方法を学びます。入力プロパティの変更を監視し、適切な処理を実行する方法について解説します。

## 学習目標
- ngOnChangesの基本的な使用方法を理解する
- 入力プロパティの変更監視方法を習得する
- SimpleChangesオブジェクトの活用方法を身につける

## 📺 画面表示用コード

```typescript
// ngOnChangesの基本実装
import { Component, Input, OnChanges, SimpleChanges } from '@angular/core';

@Component({
  selector: 'app-change-demo',
  standalone: true,
  template: `<p>値: {{value}}</p>`
})
export class ChangeDemoComponent implements OnChanges {
  @Input() value: string = '';
  
  ngOnChanges(changes: SimpleChanges) {
    console.log('入力プロパティが変更されました:', changes);
  }
}
```

```typescript
// 特定のプロパティの変更監視
ngOnChanges(changes: SimpleChanges) {
  if (changes['value']) {
    console.log('valueが変更されました');
  }
}
```

## 技術ポイント

### 1. ngOnChangesの基本
ngOnChangesは、入力プロパティが変更された時に呼び出されるLifecycle Hookです。OnChangesインターフェースを実装することで使用できます。

### 2. SimpleChangesオブジェクト
変更の詳細情報を含むオブジェクトで、以下の情報を提供します：
- `previousValue`: 変更前の値
- `currentValue`: 変更後の値
- `firstChange`: 初回変更かどうか

### 3. 変更検知のタイミング
- 入力プロパティが変更された時
- 親コンポーネントからの値の更新時
- 初期化時（firstChange = true）

## 実践的な活用例

### 1. 基本的な変更監視
```typescript
export class UserProfileComponent implements OnChanges {
  @Input() userId: string = '';
  @Input() userName: string = '';
  
  ngOnChanges(changes: SimpleChanges) {
    if (changes['userId'] && !changes['userId'].firstChange) {
      this.loadUserData(changes['userId'].currentValue);
    }
  }
  
  private loadUserData(id: string) {
    // ユーザーデータの読み込み
  }
}
```

### 2. 複数プロパティの監視
```typescript
export class DataDisplayComponent implements OnChanges {
  @Input() data: any[] = [];
  @Input() filter: string = '';
  
  ngOnChanges(changes: SimpleChanges) {
    if (changes['data'] || changes['filter']) {
      this.updateDisplay();
    }
  }
  
  private updateDisplay() {
    // 表示の更新処理
  }
}
```

## ベストプラクティス

1. **効率的な監視**: 必要なプロパティのみを監視
2. **パフォーマンス考慮**: 重い処理は避ける
3. **エラーハンドリング**: 変更処理での例外処理
4. **Signalとの組み合わせ**: Angular v20の新機能を活用

## 注意点

- 初期化時の処理（firstChange）を考慮
- パフォーマンスへの影響を意識
- 無限ループの回避
- メモリリークの防止

## 関連技術
- 入力プロパティ
- SimpleChanges
- 変更検知
- Angular v20のSignal