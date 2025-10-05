# #088 Lifecycle のテスト方法

## 概要
Angular v20におけるLifecycle Hooksのテスト方法を学びます。各Hookの動作確認、モックの使用、包括的なテストの実装方法について解説します。

## 学習目標
- Lifecycle Hooksのテスト方法を理解する
- 適切なモックの使用方法を習得する
- 包括的なテストの実装方法を身につける

## 📺 画面表示用コード

```typescript
// Lifecycle Hooksのテスト
describe('LifecycleComponent', () => {
  let component: LifecycleComponent;
  let fixture: ComponentFixture<LifecycleComponent>;
  
  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [LifecycleComponent]
    });
    fixture = TestBed.createComponent(LifecycleComponent);
    component = fixture.componentInstance;
  });
  
  it('should call ngOnInit', () => {
    spyOn(component, 'ngOnInit');
    component.ngOnInit();
    expect(component.ngOnInit).toHaveBeenCalled();
  });
  
  it('should call ngOnDestroy', () => {
    spyOn(component, 'ngOnDestroy');
    component.ngOnDestroy();
    expect(component.ngOnDestroy).toHaveBeenCalled();
  });
});
```

```typescript
// モックを使用したテスト
describe('MockedLifecycleComponent', () => {
  let component: MockedLifecycleComponent;
  let mockDataService: jasmine.SpyObj<DataService>;
  
  beforeEach(() => {
    const spy = jasmine.createSpyObj('DataService', ['getData']);
    
    TestBed.configureTestingModule({
      imports: [MockedLifecycleComponent],
      providers: [
        { provide: DataService, useValue: spy }
      ]
    });
    
    mockDataService = TestBed.inject(DataService) as jasmine.SpyObj<DataService>;
    fixture = TestBed.createComponent(MockedLifecycleComponent);
    component = fixture.componentInstance;
  });
  
  it('should load data on init', () => {
    const mockData = [{ id: 1, name: 'Test' }];
    mockDataService.getData.and.returnValue(of(mockData));
    
    component.ngOnInit();
    
    expect(mockDataService.getData).toHaveBeenCalled();
    expect(component.data).toEqual(mockData);
  });
});
```

## 技術ポイント

### 1. 基本的なテスト手法
- **Hookの実行確認**: 各Hookが適切に実行されるか
- **モックの使用**: 依存関係のモック化
- **状態の確認**: 期待される状態の確認

### 2. テストの種類
- **単体テスト**: 個別のHookのテスト
- **統合テスト**: 複数Hookの連携テスト
- **E2Eテスト**: エンドツーエンドのテスト

### 3. モックの活用
- **サービスのモック**: 外部依存のモック化
- **DOM要素のモック**: ViewChild/ViewChildrenのモック
- **イベントのモック**: イベント発火のモック

## 実践的な活用例

### 1. 包括的なLifecycleテスト
```typescript
describe('ComprehensiveLifecycleComponent', () => {
  let component: ComprehensiveLifecycleComponent;
  let fixture: ComponentFixture<ComprehensiveLifecycleComponent>;
  
  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [ComprehensiveLifecycleComponent]
    });
    fixture = TestBed.createComponent(ComprehensiveLifecycleComponent);
    component = fixture.componentInstance;
  });
  
  it('should initialize correctly', () => {
    component.ngOnInit();
    expect(component.isInitialized).toBe(true);
  });
  
  it('should handle input changes', () => {
    const changes = {
      inputValue: {
        previousValue: 'old',
        currentValue: 'new',
        firstChange: false
      }
    };
    
    component.ngOnChanges(changes);
    expect(component.processedValue).toBe('new');
  });
  
  it('should cleanup on destroy', () => {
    spyOn(component, 'cleanup');
    component.ngOnDestroy();
    expect(component.cleanup).toHaveBeenCalled();
  });
});
```

### 2. 非同期処理のテスト
```typescript
describe('AsyncLifecycleComponent', () => {
  let component: AsyncLifecycleComponent;
  let mockDataService: jasmine.SpyObj<DataService>;
  
  beforeEach(() => {
    const spy = jasmine.createSpyObj('DataService', ['getData']);
    
    TestBed.configureTestingModule({
      imports: [AsyncLifecycleComponent],
      providers: [
        { provide: DataService, useValue: spy }
      ]
    });
    
    mockDataService = TestBed.inject(DataService) as jasmine.SpyObj<DataService>;
    fixture = TestBed.createComponent(AsyncLifecycleComponent);
    component = fixture.componentInstance;
  });
  
  it('should handle async data loading', fakeAsync(() => {
    const mockData = [{ id: 1, name: 'Test' }];
    mockDataService.getData.and.returnValue(of(mockData));
    
    component.ngOnInit();
    tick();
    
    expect(component.data).toEqual(mockData);
    expect(component.loading).toBe(false);
  }));
  
  it('should handle async errors', fakeAsync(() => {
    mockDataService.getData.and.returnValue(throwError('Error'));
    
    component.ngOnInit();
    tick();
    
    expect(component.error).toBe('Error');
    expect(component.loading).toBe(false);
  }));
});
```

### 3. ViewChildのテスト
```typescript
describe('ViewChildComponent', () => {
  let component: ViewChildComponent;
  let fixture: ComponentFixture<ViewChildComponent>;
  
  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [ViewChildComponent]
    });
    fixture = TestBed.createComponent(ViewChildComponent);
    component = fixture.componentInstance;
  });
  
  it('should access ViewChild after view init', () => {
    fixture.detectChanges();
    
    expect(component.inputElement).toBeDefined();
    expect(component.inputElement?.nativeElement).toBeDefined();
  });
  
  it('should focus input after view init', () => {
    spyOn(component.inputElement?.nativeElement, 'focus');
    
    fixture.detectChanges();
    
    expect(component.inputElement?.nativeElement.focus).toHaveBeenCalled();
  });
});
```

## ベストプラクティス

1. **包括的なテスト**: 全てのHookのテスト
2. **適切なモック**: 依存関係の適切なモック化
3. **非同期処理**: 非同期処理の適切なテスト
4. **エラーケース**: エラーケースのテスト

## 注意点

- 適切なテストの分離
- モックの適切な使用
- 非同期処理の適切なテスト
- エラーケースの考慮

## 関連技術
- Angular Testing
- Jasmine
- Karma
- テスト駆動開発
