# #075 親子コンポーネントの Lifecycle 順序

## 概要
Angular v20における親子コンポーネント間のLifecycle Hooksの実行順序を学びます。複雑なコンポーネント階層での実行タイミングを理解し、適切な連携方法について解説します。

## 学習目標
- 親子コンポーネント間の実行順序を理解する
- 複数階層での実行タイミングを把握する
- 適切な親子連携の設計方法を習得する

## 📺 画面表示用コード

```typescript
// 親子コンポーネントの実行順序
export class ParentComponent implements OnInit, AfterViewInit {
  @ViewChild(ChildComponent) child?: ChildComponent;
  
  ngOnInit() {
    console.log('1. Parent ngOnInit');
  }
  
  ngAfterViewInit() {
    console.log('4. Parent ngAfterViewInit');
    this.child?.initialize();
  }
}

export class ChildComponent implements OnInit, AfterViewInit {
  ngOnInit() {
    console.log('2. Child ngOnInit');
  }
  
  ngAfterViewInit() {
    console.log('3. Child ngAfterViewInit');
  }
  
  initialize() {
    console.log('5. Child initialized by parent');
  }
}
```

```typescript
// 複数子コンポーネントの順序
export class MultiChildParentComponent implements AfterViewInit {
  @ViewChildren(ChildComponent) children?: QueryList<ChildComponent>;
  
  ngAfterViewInit() {
    this.children?.forEach((child, index) => {
      console.log(`Child ${index} ready`);
      child.setIndex(index);
    });
  }
}
```

## 技術ポイント

### 1. 基本的な親子順序
1. **親constructor** → **子constructor**
2. **親ngOnInit** → **子ngOnInit**
3. **子ngAfterViewInit** → **親ngAfterViewInit**
4. **親ngOnDestroy** → **子ngOnDestroy**

### 2. 複数子コンポーネント
- 複数の子コンポーネントは並行して初期化
- 親のngAfterViewInitで全ての子が利用可能
- ViewChildrenで複数子を管理

### 3. 深い階層での順序
- 深い階層でも基本的な順序は維持
- 各階層で適切な連携が必要

## 実践的な活用例

### 1. 親子データ連携
```typescript
export class DataParentComponent implements OnInit, AfterViewInit {
  @Input() initialData: any;
  @ViewChild(DataChildComponent) child?: DataChildComponent;
  
  ngOnInit() {
    console.log('Parent: データ準備');
  }
  
  ngAfterViewInit() {
    if (this.child && this.initialData) {
      this.child.loadData(this.initialData);
    }
  }
}

export class DataChildComponent implements OnInit {
  private data: any;
  
  ngOnInit() {
    console.log('Child: 準備完了');
  }
  
  loadData(data: any) {
    this.data = data;
    console.log('Child: データ受信');
  }
}
```

### 2. フォームコンポーネントの連携
```typescript
export class FormParentComponent implements AfterViewInit {
  @ViewChildren(FormFieldComponent) fields?: QueryList<FormFieldComponent>;
  
  ngAfterViewInit() {
    this.setupFormValidation();
  }
  
  private setupFormValidation() {
    this.fields?.forEach(field => {
      field.setValidationRules();
    });
  }
}
```

### 3. 動的コンテンツの管理
```typescript
export class DynamicParentComponent implements AfterViewInit {
  @ViewChildren(DynamicChildComponent) children?: QueryList<DynamicChildComponent>;
  
  ngAfterViewInit() {
    this.children?.changes.subscribe(() => {
      this.updateLayout();
    });
  }
  
  private updateLayout() {
    // レイアウトの更新
  }
}
```

## ベストプラクティス

1. **順序の理解**: 親子間の実行順序を正確に把握
2. **適切な連携**: 各段階での適切な親子連携
3. **データフロー**: 適切なデータの流れの設計
4. **パフォーマンス**: 効率的な親子連携

## 注意点

- 実行順序への過度な依存を避ける
- 適切なタイミングでの親子連携
- 循環参照の回避
- パフォーマンスへの影響を考慮

## 関連技術
- 親子コンポーネント
- ViewChild/ViewChildren
- データフロー
- コンポーネント設計
