# #159 「ViewChild/ContentChild のテスト」

## 概要
Angular v20におけるViewChildとContentChildのテスト実装方法。ComponentFixtureとDebugElementを使用して、参照の存在確認と動作検証を行うテスト手法を学ぶ。

## 学習目標
- ViewChild/ContentChildのテスト方法を理解する
- ComponentFixtureでの要素取得を学ぶ
- 参照の動作検証を把握する

## 技術ポイント
- ComponentFixture.query() での要素取得
- DebugElement の活用
- 参照の存在確認
- 動作の検証

## 📺 画面表示用コード

### テスト対象コンポーネント
```typescript
@Component({
  selector: 'app-testable-child',
  template: `<div>テスト対象子コンポーネント</div>`
})
export class TestableChildComponent {
  testMethod() {
    return 'テストメソッド実行';
  }
}

@Component({
  selector: 'app-testable-parent',
  template: `
    <app-testable-child #childRef></app-testable-child>
    <div #contentRef>コンテンツ要素</div>
  `
})
export class TestableParentComponent implements AfterViewInit {
  @ViewChild('childRef') childComponent!: TestableChildComponent;
  @ViewChild('contentRef') contentElement!: ElementRef;

  ngAfterViewInit() {
    console.log('テスト対象準備完了');
  }

  callChildMethod() {
    return this.childComponent.testMethod();
  }
}
```

### テスト実装
```typescript
describe('TestableParentComponent', () => {
  let component: TestableParentComponent;
  let fixture: ComponentFixture<TestableParentComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [TestableParentComponent, TestableChildComponent]
    });
    fixture = TestBed.createComponent(TestableParentComponent);
    component = fixture.componentInstance;
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should have ViewChild references', () => {
    fixture.detectChanges();
    
    expect(component.childComponent).toBeTruthy();
    expect(component.contentElement).toBeTruthy();
  });

  it('should call child method', () => {
    fixture.detectChanges();
    
    const result = component.callChildMethod();
    expect(result).toBe('テストメソッド実行');
  });

  it('should access DOM element', () => {
    fixture.detectChanges();
    
    const element = component.contentElement.nativeElement;
    expect(element.textContent).toContain('コンテンツ要素');
  });
});
```

## 実践的な活用例
- 参照の存在確認
- メソッド呼び出しのテスト
- DOM要素の検証

## ベストプラクティス
- 適切なテストデータの準備
- 非同期処理の考慮
- クリーンアップの実装

## 注意点
- ライフサイクルのタイミング
- 動的要素のテスト
- メモリリークの防止

## 関連技術
- ユニットテスト
- ComponentFixture
- DebugElement
