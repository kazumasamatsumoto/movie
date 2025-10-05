# #136 「ViewChild read オプション」

## 概要
Angular v20におけるViewChildのreadオプションの使用方法。参照する要素の型を明示的に指定し、ElementRef、ViewContainerRef、TemplateRefなど、取得したい具体的な型を制御する方法を学ぶ。

## 学習目標
- readオプションの基本的な使い方を理解する
- 取得可能な型の種類を学ぶ
- 型安全性の向上方法を把握する

## 技術ポイント
- read: ElementRef でのDOM要素取得
- read: ViewContainerRef でのビューコンテナ取得
- read: TemplateRef でのテンプレート取得
- 型安全性の確保

## 📺 画面表示用コード

### ElementRefでの取得
```typescript
@Component({
  selector: 'app-element-ref',
  template: `
    <div #myDiv class="element">ElementRefの例</div>
    <button (click)="manipulateElement()">要素操作</button>
  `,
  styles: [`
    .element {
      padding: 10px;
      border: 1px solid #ccc;
      margin: 10px 0;
    }
  `]
})
export class ElementRefComponent implements AfterViewInit {
  @ViewChild('myDiv', { read: ElementRef }) myDiv!: ElementRef<HTMLDivElement>;
  
  ngAfterViewInit() {
    console.log('ElementRef:', this.myDiv.nativeElement);
  }
  
  manipulateElement() {
    const element = this.myDiv.nativeElement;
    element.style.backgroundColor = 'lightblue';
    element.style.padding = '20px';
    element.textContent = 'ElementRefで操作されました';
  }
}
```

### ViewContainerRefでの取得
```typescript
@Component({
  selector: 'app-view-container',
  template: `
    <ng-container #containerRef></ng-container>
    <button (click)="createComponent()">コンポーネント作成</button>
  `
})
export class ViewContainerComponent implements AfterViewInit {
  @ViewChild('containerRef', { read: ViewContainerRef }) 
  container!: ViewContainerRef;
  
  ngAfterViewInit() {
    console.log('ViewContainerRef:', this.container);
  }
  
  createComponent() {
    // 動的コンポーネントの作成例
    const componentRef = this.container.createComponent(DynamicComponent);
    componentRef.instance.data = '動的に作成されたコンポーネント';
  }
}
```

### TemplateRefでの取得
```typescript
@Component({
  selector: 'app-template-ref',
  template: `
    <ng-template #myTemplate let-data="data">
      <div>テンプレートデータ: {{ data }}</div>
    </ng-template>
    <button (click)="renderTemplate()">テンプレート描画</button>
    <div #templateContainer></div>
  `
})
export class TemplateRefComponent implements AfterViewInit {
  @ViewChild('myTemplate', { read: TemplateRef }) 
  myTemplate!: TemplateRef<any>;
  
  @ViewChild('templateContainer', { read: ViewContainerRef }) 
  container!: ViewContainerRef;
  
  ngAfterViewInit() {
    console.log('TemplateRef:', this.myTemplate);
  }
  
  renderTemplate() {
    this.container.clear();
    this.container.createEmbeddedView(this.myTemplate, {
      data: 'テンプレートから渡されたデータ'
    });
  }
}
```

## 実践的な活用例
- 動的コンポーネントの作成
- テンプレートの再利用
- DOM要素の直接操作

## ベストプラクティス
- 適切な型を指定する
- 型安全性を保つ
- 用途に応じてreadオプションを選択する

## 注意点
- 指定した型が存在しない場合のエラー
- プラットフォーム非依存な実装を心がける
- パフォーマンスを考慮する

## 関連技術
- ElementRef
- ViewContainerRef
- TemplateRef
- 型安全性
