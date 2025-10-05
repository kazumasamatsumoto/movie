# #084 Lifecycle のデバッグ方法

## 概要
Angular v20におけるLifecycle Hooksのデバッグ方法を学びます。実行順序の確認、パフォーマンス問題の特定、適切なデバッグ手法について解説します。

## 学習目標
- Lifecycle Hooksのデバッグ方法を理解する
- 実行順序の確認方法を習得する
- パフォーマンス問題の特定方法を身につける

## 📺 画面表示用コード

```typescript
// デバッグ用のログ出力
export class DebugLifecycleComponent implements 
  OnInit, OnDestroy, OnChanges {
  
  ngOnInit() {
    console.log('🔵 ngOnInit実行:', this.constructor.name);
    console.time('component-init');
  }
  
  ngOnChanges(changes: SimpleChanges) {
    console.log('🟡 ngOnChanges実行:', changes);
  }
  
  ngOnDestroy() {
    console.log('🔴 ngOnDestroy実行:', this.constructor.name);
    console.timeEnd('component-init');
  }
}
```

```typescript
// パフォーマンス監視
export class PerformanceDebugComponent implements DoCheck {
  private checkCount = 0;
  
  ngDoCheck() {
    this.checkCount++;
    if (this.checkCount % 10 === 0) {
      console.warn(`⚠️ ngDoCheckが${this.checkCount}回実行されました`);
    }
  }
}
```

## 技術ポイント

### 1. 基本的なデバッグ手法
- **ログ出力**: console.logでの実行確認
- **タイミング測定**: console.time/timeEndでの時間測定
- **実行回数カウント**: 実行回数の監視

### 2. 実行順序の確認
- 親子コンポーネント間の実行順序
- 各Hookの実行タイミング
- 変更検知サイクルの確認

### 3. パフォーマンス監視
- 頻繁に実行されるHookの監視
- 処理時間の測定
- メモリ使用量の監視

## 実践的な活用例

### 1. 包括的なデバッグ
```typescript
export class ComprehensiveDebugComponent implements 
  OnInit, OnDestroy, OnChanges, DoCheck {
  
  private lifecycleLog: string[] = [];
  
  ngOnInit() {
    this.logLifecycle('ngOnInit');
    console.time('component-lifecycle');
  }
  
  ngOnChanges(changes: SimpleChanges) {
    this.logLifecycle('ngOnChanges', changes);
  }
  
  ngDoCheck() {
    this.logLifecycle('ngDoCheck');
  }
  
  ngOnDestroy() {
    this.logLifecycle('ngOnDestroy');
    console.timeEnd('component-lifecycle');
    console.log('📋 ライフサイクルログ:', this.lifecycleLog);
  }
  
  private logLifecycle(hook: string, data?: any) {
    const timestamp = new Date().toISOString();
    const log = `${timestamp} - ${hook}`;
    this.lifecycleLog.push(log);
    console.log(`🔄 ${log}`, data || '');
  }
}
```

### 2. パフォーマンス監視
```typescript
export class PerformanceMonitorComponent implements DoCheck {
  private checkTimes: number[] = [];
  private maxChecks = 100;
  
  ngDoCheck() {
    const startTime = performance.now();
    
    // 実際の処理
    this.performCheck();
    
    const endTime = performance.now();
    const duration = endTime - startTime;
    
    this.checkTimes.push(duration);
    
    if (this.checkTimes.length > this.maxChecks) {
      this.checkTimes.shift();
    }
    
    if (duration > 10) { // 10ms以上
      console.warn(`⚠️ 遅いngDoCheck: ${duration.toFixed(2)}ms`);
    }
  }
  
  private performCheck() {
    // チェック処理
  }
}
```

### 3. 親子コンポーネントのデバッグ
```typescript
export class ParentDebugComponent implements OnInit, AfterViewInit {
  @ViewChild(ChildDebugComponent) child?: ChildDebugComponent;
  
  ngOnInit() {
    console.log('👨‍👩‍👧‍👦 Parent ngOnInit');
  }
  
  ngAfterViewInit() {
    console.log('👨‍👩‍👧‍👦 Parent ngAfterViewInit');
    if (this.child) {
      console.log('👶 Child component ready');
    }
  }
}

export class ChildDebugComponent implements OnInit, AfterViewInit {
  ngOnInit() {
    console.log('👶 Child ngOnInit');
  }
  
  ngAfterViewInit() {
    console.log('👶 Child ngAfterViewInit');
  }
}
```

## ベストプラクティス

1. **適切なログレベル**: 本番環境でのログ出力制御
2. **パフォーマンス監視**: 定期的なパフォーマンスチェック
3. **構造化ログ**: 構造化されたログ出力
4. **デバッグツール**: Angular DevToolsの活用

## 注意点

- 本番環境でのログ出力制御
- パフォーマンスへの影響を考慮
- 機密情報のログ出力回避
- 適切なデバッグレベルの設定

## 関連技術
- デバッグ手法
- パフォーマンス監視
- ログ管理
- Angular DevTools
