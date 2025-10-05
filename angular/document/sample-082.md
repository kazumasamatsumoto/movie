# #082 Lifecycle でのイベントリスナー登録

## 概要
Angular v20におけるLifecycle Hooksでのイベントリスナー登録を学びます。適切なタイミングでのイベントリスナーの登録と削除、メモリリークを防ぐ方法について解説します。

## 学習目標
- イベントリスナー登録の基本を理解する
- 適切な登録・削除のタイミングを把握する
- メモリリークを防ぐ管理方法を習得する

## 📺 画面表示用コード

```typescript
// イベントリスナー登録の基本
export class EventListenerComponent implements OnInit, OnDestroy {
  private resizeListener?: () => void;
  private scrollListener?: () => void;
  
  ngOnInit() {
    this.registerEventListeners();
  }
  
  ngOnDestroy() {
    this.removeEventListeners();
  }
  
  private registerEventListeners() {
    this.resizeListener = () => this.onResize();
    this.scrollListener = () => this.onScroll();
    
    window.addEventListener('resize', this.resizeListener);
    window.addEventListener('scroll', this.scrollListener);
  }
  
  private removeEventListeners() {
    if (this.resizeListener) {
      window.removeEventListener('resize', this.resizeListener);
    }
    if (this.scrollListener) {
      window.removeEventListener('scroll', this.scrollListener);
    }
  }
}
```

```typescript
// 複数イベントの管理
export class MultipleEventComponent implements OnInit, OnDestroy {
  private eventListeners = new Map<string, () => void>();
  
  ngOnInit() {
    this.registerAllEventListeners();
  }
  
  ngOnDestroy() {
    this.removeAllEventListeners();
  }
  
  private registerAllEventListeners() {
    const events = ['resize', 'scroll', 'click', 'keydown'];
    
    events.forEach(eventType => {
      const listener = () => this.handleEvent(eventType);
      this.eventListeners.set(eventType, listener);
      window.addEventListener(eventType, listener);
    });
  }
}
```

## 技術ポイント

### 1. イベントリスナー登録の基本
- **適切なタイミング**: ngOnInitでの登録
- **適切な削除**: ngOnDestroyでの削除
- **メモリリークの防止**: 確実な削除

### 2. 登録・削除のパターン
- **個別管理**: 各イベントの個別管理
- **集約管理**: 複数イベントの集約管理
- **自動管理**: 自動的な登録・削除

### 3. パフォーマンス考慮
- 適切なイベントの選択
- 効率的なイベントハンドリング
- 不要なイベントの回避

## 実践的な活用例

### 1. ウィンドウイベントの管理
```typescript
export class WindowEventComponent implements OnInit, OnDestroy {
  private eventListeners = new Map<string, () => void>();
  
  ngOnInit() {
    this.registerWindowEvents();
  }
  
  ngOnDestroy() {
    this.removeWindowEvents();
  }
  
  private registerWindowEvents() {
    const events = {
      'resize': () => this.onWindowResize(),
      'scroll': () => this.onWindowScroll(),
      'beforeunload': () => this.onBeforeUnload()
    };
    
    Object.entries(events).forEach(([eventType, handler]) => {
      this.eventListeners.set(eventType, handler);
      window.addEventListener(eventType, handler);
    });
  }
  
  private removeWindowEvents() {
    this.eventListeners.forEach((handler, eventType) => {
      window.removeEventListener(eventType, handler);
    });
    this.eventListeners.clear();
  }
}
```

### 2. カスタムイベントの管理
```typescript
export class CustomEventComponent implements OnInit, OnDestroy {
  private customEventListeners = new Map<string, (event: CustomEvent) => void>();
  
  ngOnInit() {
    this.registerCustomEvents();
  }
  
  ngOnDestroy() {
    this.removeCustomEvents();
  }
  
  private registerCustomEvents() {
    const events = {
      'dataLoaded': (event: CustomEvent) => this.onDataLoaded(event),
      'userAction': (event: CustomEvent) => this.onUserAction(event)
    };
    
    Object.entries(events).forEach(([eventType, handler]) => {
      this.customEventListeners.set(eventType, handler);
      document.addEventListener(eventType, handler);
    });
  }
  
  private removeCustomEvents() {
    this.customEventListeners.forEach((handler, eventType) => {
      document.removeEventListener(eventType, handler);
    });
    this.customEventListeners.clear();
  }
}
```

### 3. 条件付きイベント登録
```typescript
export class ConditionalEventComponent implements OnInit, OnDestroy {
  @Input() enableKeyboardEvents = false;
  private keyboardListener?: (event: KeyboardEvent) => void;
  
  ngOnInit() {
    if (this.enableKeyboardEvents) {
      this.registerKeyboardEvents();
    }
  }
  
  ngOnDestroy() {
    if (this.keyboardListener) {
      document.removeEventListener('keydown', this.keyboardListener);
    }
  }
  
  private registerKeyboardEvents() {
    this.keyboardListener = (event: KeyboardEvent) => {
      this.handleKeyboardEvent(event);
    };
    document.addEventListener('keydown', this.keyboardListener);
  }
  
  private handleKeyboardEvent(event: KeyboardEvent) {
    // キーボードイベントの処理
  }
}
```

## ベストプラクティス

1. **適切な管理**: イベントリスナーの適切な登録・削除
2. **メモリリーク防止**: 確実な削除によるメモリリーク防止
3. **効率的な処理**: 効率的なイベントハンドリング
4. **条件付き登録**: 必要な時のみイベント登録

## 注意点

- 全てのイベントリスナーを適切に削除
- メモリリークの防止
- 適切なタイミングでの登録・削除
- パフォーマンスへの影響を考慮

## 関連技術
- イベント管理
- メモリ管理
- パフォーマンス最適化
- カスタムイベント
