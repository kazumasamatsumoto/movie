# #217 「コンテンツ投影のテスト」

## 概要
Angular v20のコンテンツ投影コンポーネントのテスト手法を学習します。

## 学習目標
- コンテンツ投影のテスト手法を理解する
- JasmineとKarmaを使用したテストを習得する
- 品質の高いコンテンツ投影コンポーネントを実現できるようになる

## 技術ポイント
- コンテンツ投影テスト
- Jasmine/Karma
- コンポーネントテスト

## 📺 画面表示用コード

```typescript
// テスト対象のコンポーネント
@Component({
  selector: 'app-testable-content',
  template: `
    <div class="container">
      <ng-content></ng-content>
    </div>
  `
})
export class TestableContentComponent {
  @ContentChild('projectedContent') projectedContent!: ElementRef;
  
  ngAfterContentInit() {
    if (this.projectedContent) {
      this.projectedContent.nativeElement.classList.add('initialized');
    }
  }
}
```

```typescript
// テストファイル
describe('TestableContentComponent', () => {
  let component: TestableContentComponent;
  let fixture: ComponentFixture<TestableContentComponent>;
  
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TestableContentComponent]
    }).compileComponents();
    
    fixture = TestBed.createComponent(TestableContentComponent);
    component = fixture.componentInstance;
  });
  
  it('投影されたコンテンツを正しく表示する', () => {
    fixture.detectChanges();
    
    const compiled = fixture.nativeElement;
    const contentElement = compiled.querySelector('.container');
    
    expect(contentElement).toBeTruthy();
  });
  
  it('投影されたコンテンツにアクセスできる', () => {
    fixture.detectChanges();
    
    expect(component.projectedContent).toBeDefined();
  });
});
```

```html
<!-- テスト用テンプレート -->
<app-testable-content>
  <div #projectedContent class="test-content">
    テストコンテンツ
  </div>
</app-testable-content>
```

## 実践的な活用例

```typescript
// 複雑なコンテンツ投影のテスト
describe('MultiSlotComponent', () => {
  it('複数のスロットに正しくコンテンツを投影する', () => {
    const fixture = TestBed.createComponent(MultiSlotComponent);
    
    // テストデータを設定
    fixture.componentInstance.items = [
      { id: 1, name: 'アイテム1' },
      { id: 2, name: 'アイテム2' }
    ];
    
    fixture.detectChanges();
    
    const compiled = fixture.nativeElement;
    const projectedItems = compiled.querySelectorAll('.projected-item');
    
    expect(projectedItems.length).toBe(2);
  });
});
```

## ベストプラクティス
- 投影されるコンテンツのテストを網羅する
- モックデータを使用してテストする
- エッジケースを考慮したテストを作成する
- テストの可読性を重視する

## 注意点
- 投影コンテンツの初期化タイミング
- テスト環境でのDOM操作
- 非同期処理のテスト

## 関連技術
- Jasmine Testing
- Karma Test Runner
- Angular Testing Utilities
