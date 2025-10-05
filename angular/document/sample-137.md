# #137 「ViewChild static オプション」

## 概要
Angular v20におけるViewChildのstaticオプションの使用方法。要素の検索タイミングを制御し、static:trueならngOnInitで、static:falseならngAfterViewInitで要素を検索する設定方法を学ぶ。

## 学習目標
- staticオプションの基本的な使い方を理解する
- 検索タイミングの違いを学ぶ
- 適切な設定方法を把握する

## 技術ポイント
- static: true でのngOnInit検索
- static: false でのngAfterViewInit検索
- 動的要素の扱い
- パフォーマンスの考慮

## 📺 画面表示用コード

### static: true の使用例
```typescript
@Component({
  selector: 'app-static-true',
  template: `
    <div #staticElement>静的要素（常に存在）</div>
    <button (click)="accessStaticElement()">静的要素アクセス</button>
  `
})
export class StaticTrueComponent implements OnInit, AfterViewInit {
  @ViewChild('staticElement', { static: true }) 
  staticElement!: ElementRef<HTMLDivElement>;
  
  ngOnInit() {
    // static: true なので ngOnInit で使用可能
    console.log('ngOnInit - 静的要素:', this.staticElement.nativeElement);
    this.staticElement.nativeElement.style.color = 'blue';
  }
  
  ngAfterViewInit() {
    console.log('ngAfterViewInit - 静的要素:', this.staticElement.nativeElement);
  }
  
  accessStaticElement() {
    this.staticElement.nativeElement.style.backgroundColor = 'lightgreen';
  }
}
```

### static: false の使用例
```typescript
@Component({
  selector: 'app-static-false',
  template: `
    <div *ngIf="showDynamicElement" #dynamicElement>
      動的要素（条件付きで表示）
    </div>
    <button (click)="toggleElement()">要素表示切り替え</button>
    <button (click)="accessDynamicElement()">動的要素アクセス</button>
  `
})
export class StaticFalseComponent implements OnInit, AfterViewInit {
  @ViewChild('dynamicElement', { static: false }) 
  dynamicElement!: ElementRef<HTMLDivElement>;
  
  showDynamicElement = false;
  
  ngOnInit() {
    // static: false なので ngOnInit では未初期化
    console.log('ngOnInit - 動的要素:', this.dynamicElement); // undefined
  }
  
  ngAfterViewInit() {
    // static: false なので ngAfterViewInit で使用可能
    if (this.dynamicElement) {
      console.log('ngAfterViewInit - 動的要素:', this.dynamicElement.nativeElement);
    } else {
      console.log('動的要素はまだ表示されていません');
    }
  }
  
  toggleElement() {
    this.showDynamicElement = !this.showDynamicElement;
  }
  
  accessDynamicElement() {
    if (this.dynamicElement) {
      this.dynamicElement.nativeElement.style.backgroundColor = 'lightcoral';
    } else {
      console.log('動的要素が存在しません');
    }
  }
}
```

### 混合使用例
```typescript
@Component({
  selector: 'app-mixed-usage',
  template: `
    <div #staticRef>静的参照</div>
    <div *ngIf="showDynamic" #dynamicRef>動的参照</div>
    <button (click)="toggleDynamic()">動的要素切り替え</button>
  `
})
export class MixedUsageComponent implements OnInit, AfterViewInit {
  // 静的要素は static: true
  @ViewChild('staticRef', { static: true }) 
  staticRef!: ElementRef;
  
  // 動的要素は static: false
  @ViewChild('dynamicRef', { static: false }) 
  dynamicRef!: ElementRef;
  
  showDynamic = false;
  
  ngOnInit() {
    // 静的要素のみ使用可能
    this.staticRef.nativeElement.style.color = 'blue';
  }
  
  ngAfterViewInit() {
    // 両方の要素が使用可能
    if (this.dynamicRef) {
      this.dynamicRef.nativeElement.style.color = 'red';
    }
  }
  
  toggleDynamic() {
    this.showDynamic = !this.showDynamic;
  }
}
```

## 実践的な活用例
- 常に存在する要素の初期設定
- 条件付き表示要素の制御
- フォーム要素の初期化

## ベストプラクティス
- 要素の存在条件に応じて適切に選択する
- パフォーマンスを考慮する
- 明確な命名規則を使用する

## 注意点
- static: trueは常に存在する要素のみ
- static: falseは動的要素に対応
- 適切なライフサイクルでの使用

## 関連技術
- コンポーネントライフサイクル
- 動的要素
- パフォーマンス最適化
- 要素検索
