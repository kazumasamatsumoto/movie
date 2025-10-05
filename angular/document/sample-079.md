# #079 Lifecycle でのタイマー処理

## 概要
Angular v20におけるLifecycle Hooksでのタイマー処理を学びます。setInterval/setTimeoutの適切な管理とクリーンアップ方法について解説します。

## 学習目標
- タイマー処理の基本を理解する
- 適切なタイマー管理方法を習得する
- メモリリークを防ぐクリーンアップ方法を身につける

## 📺 画面表示用コード

```typescript
// タイマー処理の基本
export class TimerComponent implements OnInit, OnDestroy {
  private timer?: number;
  private interval?: number;
  
  ngOnInit() {
    // setTimeout
    this.timer = setTimeout(() => {
      this.delayedAction();
    }, 1000);
    
    // setInterval
    this.interval = setInterval(() => {
      this.periodicAction();
    }, 1000);
  }
  
  ngOnDestroy() {
    if (this.timer) {
      clearTimeout(this.timer);
    }
    if (this.interval) {
      clearInterval(this.interval);
    }
  }
}
```

```typescript
// 複数タイマーの管理
export class MultipleTimerComponent implements OnInit, OnDestroy {
  private timers: number[] = [];
  
  ngOnInit() {
    this.timers.push(
      setTimeout(() => this.action1(), 1000)
    );
    this.timers.push(
      setInterval(() => this.action2(), 2000)
    );
  }
  
  ngOnDestroy() {
    this.timers.forEach(timer => {
      clearTimeout(timer);
      clearInterval(timer);
    });
  }
}
```

## 技術ポイント

### 1. タイマー処理の基本
- **setTimeout**: 遅延実行
- **setInterval**: 定期実行
- **clearTimeout/clearInterval**: タイマーのクリア

### 2. 適切な管理
- タイマーIDの保存
- 適切なクリーンアップ
- 複数タイマーの管理

### 3. メモリリークの防止
- ngOnDestroyでの確実なクリア
- タイマーの適切な管理
- リソースの解放

## 実践的な活用例

### 1. カウントダウンタイマー
```typescript
export class CountdownComponent implements OnInit, OnDestroy {
  countdown = 60;
  private timer?: number;
  
  ngOnInit() {
    this.startCountdown();
  }
  
  ngOnDestroy() {
    if (this.timer) {
      clearInterval(this.timer);
    }
  }
  
  private startCountdown() {
    this.timer = setInterval(() => {
      this.countdown--;
      if (this.countdown <= 0) {
        this.onCountdownComplete();
        clearInterval(this.timer!);
      }
    }, 1000);
  }
  
  private onCountdownComplete() {
    console.log('カウントダウン完了');
  }
}
```

### 2. 自動保存機能
```typescript
export class AutoSaveComponent implements OnInit, OnDestroy {
  private saveTimer?: number;
  private saveInterval = 30000; // 30秒
  
  ngOnInit() {
    this.startAutoSave();
  }
  
  ngOnDestroy() {
    if (this.saveTimer) {
      clearInterval(this.saveTimer);
    }
  }
  
  private startAutoSave() {
    this.saveTimer = setInterval(() => {
      this.saveData();
    }, this.saveInterval);
  }
  
  private saveData() {
    // 自動保存処理
    console.log('データを自動保存しました');
  }
}
```

### 3. デバウンス処理
```typescript
export class DebounceComponent implements OnInit, OnDestroy {
  private debounceTimer?: number;
  
  ngOnInit() {
    // 初期化処理
  }
  
  ngOnDestroy() {
    if (this.debounceTimer) {
      clearTimeout(this.debounceTimer);
    }
  }
  
  onInputChange() {
    if (this.debounceTimer) {
      clearTimeout(this.debounceTimer);
    }
    
    this.debounceTimer = setTimeout(() => {
      this.processInput();
    }, 300);
  }
  
  private processInput() {
    // 入力処理
  }
}
```

## ベストプラクティス

1. **適切なクリーンアップ**: ngOnDestroyでの確実なタイマークリア
2. **効率的な管理**: 複数タイマーの効率的な管理
3. **エラーハンドリング**: タイマー処理での例外処理
4. **パフォーマンス**: 不要なタイマーの早期停止

## 注意点

- 全てのタイマーを適切にクリア
- メモリリークの防止
- 適切なタイミングでのタイマー停止
- エラーハンドリングの実装

## 関連技術
- タイマー管理
- メモリ管理
- デバウンス処理
- 自動保存機能
