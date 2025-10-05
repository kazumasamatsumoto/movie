# #061 Lifecycle Hooks とは？コンポーネントの一生

## 概要
Angular v20におけるLifecycle Hooksの基本概念を学びます。コンポーネントの一生を通じて、適切なタイミングで処理を実行する方法について解説します。

## 学習目標
- Lifecycle Hooksの基本概念を理解する
- コンポーネントの各段階を把握する
- 適切なタイミングでの処理実行方法を習得する

## 📺 画面表示用コード

```typescript
// Lifecycle Hooksの基本実装
import { Component, OnInit, OnDestroy } from '@angular/core';

@Component({
  selector: 'app-lifecycle-demo',
  standalone: true,
  template: `<p>{{message}}</p>`
})
export class LifecycleDemoComponent implements OnInit, OnDestroy {
  message = 'コンポーネントの一生を管理します';
  
  ngOnInit() {
    console.log('コンポーネントが初期化されました');
  }
  
  ngOnDestroy() {
    console.log('コンポーネントが破棄されました');
  }
}
```

```typescript
// 主要なLifecycle Hooks
export class ComponentLifecycle implements OnInit, OnDestroy {
  ngOnInit() {
    // 初期化処理
  }
  
  ngOnDestroy() {
    // クリーンアップ処理
  }
}
```

## 技術ポイント

### 1. Lifecycle Hooksの基本概念
Lifecycle Hooksは、Angularコンポーネントの各段階で実行されるメソッドです。コンポーネントの一生を通じて、適切なタイミングで処理を実行できます。

### 2. 主要な段階
- **初期化**: コンポーネントの作成と設定
- **変更検知**: データの変更を監視
- **ビュー更新**: DOMの更新
- **破棄**: コンポーネントのクリーンアップ

### 3. Angular v20での改善
- Signalベースのリアクティブシステムとの統合
- パフォーマンスの向上
- より直感的なAPI

## 実践的な活用例

### 1. 基本的なLifecycle管理
```typescript
export class BasicLifecycleComponent implements OnInit, OnDestroy {
  private timer?: number;
  
  ngOnInit() {
    this.timer = setInterval(() => {
      console.log('定期実行');
    }, 1000);
  }
  
  ngOnDestroy() {
    if (this.timer) {
      clearInterval(this.timer);
    }
  }
}
```

### 2. リソース管理
```typescript
export class ResourceManagementComponent implements OnInit, OnDestroy {
  private subscriptions = new Set<Subscription>();
  
  ngOnInit() {
    const sub = this.dataService.getData().subscribe();
    this.subscriptions.add(sub);
  }
  
  ngOnDestroy() {
    this.subscriptions.forEach(sub => sub.unsubscribe());
  }
}
```

## ベストプラクティス

1. **適切なタイミング**: 各段階で適切な処理を実行
2. **リソース管理**: メモリリークを防ぐためのクリーンアップ
3. **パフォーマンス考慮**: 不要な処理を避ける
4. **Signalとの組み合わせ**: Angular v20の新機能を活用

## 注意点

- メモリリークの防止
- 適切なクリーンアップ処理
- パフォーマンスへの影響を考慮
- Angular v20の新機能との組み合わせ

## 関連技術
- コンポーネント
- Angular v20のSignal
- メモリ管理
- パフォーマンス最適化
