# #121 「Input/Output のテスト方法」

## 概要
Angular v20におけるInput/Outputのテスト実装方法。ComponentFixtureとDebugElementを活用して、コンポーネントの動作を確実に検証し、品質の高いアプリケーションを構築するためのテスト手法を学ぶ。

## 学習目標
- Input/Outputの基本的なテスト方法を理解する
- ComponentFixtureとDebugElementの使い方を学ぶ
- モックとスパイを活用したテスト実装を把握する

## 技術ポイント
- ComponentFixture を使ったテスト環境の構築
- DebugElement によるDOM操作のテスト
- モックとスパイの活用
- イベント発火のテスト

## 📺 画面表示用コード

### テスト対象コンポーネント
```typescript
@Component({
  selector: 'app-testable-component',
  template: `
    <div>{{ message }}</div>
    <button (click)="sendMessage()">送信</button>
  `
})
export class TestableComponent {
  @Input() message: string = '';
  @Output() messageChange = new EventEmitter<string>();

  sendMessage() {
    this.messageChange.emit('Test Message');
  }
}
```

### テスト実装
```typescript
describe('TestableComponent', () => {
  let component: TestableComponent;
  let fixture: ComponentFixture<TestableComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [TestableComponent]
    });
    fixture = TestBed.createComponent(TestableComponent);
    component = fixture.componentInstance;
  });

  it('should display input message', () => {
    component.message = 'Hello Test';
    fixture.detectChanges();
    
    const compiled = fixture.nativeElement;
    expect(compiled.textContent).toContain('Hello Test');
  });

  it('should emit event when button clicked', () => {
    spyOn(component.messageChange, 'emit');
    
    component.sendMessage();
    
    expect(component.messageChange.emit).toHaveBeenCalledWith('Test Message');
  });
});
```

## 実践的な活用例
- フォームコンポーネントのテスト
- リストコンポーネントのテスト
- モーダルコンポーネントのテスト

## ベストプラクティス
- 適切なモックとスパイを使用する
- テストケースを明確に分離する
- 非同期処理のテストを適切に行う
- テストデータを適切に管理する

## 注意点
- テスト環境の設定を適切に行う
- メモリリークを防ぐため、適切なクリーンアップを行う
- テストの実行時間を考慮する

## 関連技術
- Jasmine
- Karma
- Angular Testing Utilities
- ユニットテスト
