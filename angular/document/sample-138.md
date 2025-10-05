# #138 「ViewChild とライフサイクル」

## 概要
Angular v20におけるViewChildとコンポーネントライフサイクルの関係。ngOnInit、ngAfterViewInit、ngAfterViewCheckedなど、適切なライフサイクルでのViewChildの使用タイミングを理解し、エラーを回避する方法を学ぶ。

## 学習目標
- ViewChildとライフサイクルの関係を理解する
- 適切な使用タイミングを学ぶ
- エラー回避の方法を把握する

## 技術ポイント
- ngOnInit での制限
- ngAfterViewInit での安全な使用
- ngAfterViewChecked での変更検知
- ライフサイクルの順序

## 📺 画面表示用コード

### ライフサイクルでのViewChild使用
```typescript
@Component({
  selector: 'app-lifecycle',
  template: `
    <div #myElement>ライフサイクル要素</div>
    <button (click)="updateElement()">要素更新</button>
  `
})
export class LifecycleComponent implements 
  OnInit, AfterViewInit, AfterViewChecked {
  
  @ViewChild('myElement') myElement!: ElementRef;
  updateCount = 0;
  
  ngOnInit() {
    console.log('ngOnInit - ViewChild:', this.myElement);
    // ViewChildはまだ未初期化（undefined）
    // this.myElement.nativeElement; // エラーになる
    
    // 静的要素のみ使用可能（static: trueの場合）
  }
  
  ngAfterViewInit() {
    console.log('ngAfterViewInit - ViewChild:', this.myElement);
    // ViewChildが初期化完了、安全に使用可能
    if (this.myElement) {
      this.myElement.nativeElement.style.color = 'blue';
    }
  }
  
  ngAfterViewChecked() {
    console.log('ngAfterViewChecked - ビューの変更検知');
    // ビューが更新された後に呼ばれる
    // 無限ループに注意
  }
  
  updateElement() {
    if (this.myElement) {
      this.updateCount++;
      this.myElement.nativeElement.textContent = 
        `更新回数: ${this.updateCount}`;
    }
  }
}
```

### 動的要素のライフサイクル対応
```typescript
@Component({
  selector: 'app-dynamic-lifecycle',
  template: `
    <div *ngIf="showElement" #dynamicElement>
      動的要素
    </div>
    <button (click)="toggleElement()">要素切り替え</button>
    <button (click)="accessElement()">要素アクセス</button>
  `
})
export class DynamicLifecycleComponent implements 
  OnInit, AfterViewInit, AfterViewChecked {
  
  @ViewChild('dynamicElement', { static: false }) 
  dynamicElement!: ElementRef;
  
  showElement = false;
  
  ngOnInit() {
    console.log('ngOnInit - 動的要素:', this.dynamicElement);
  }
  
  ngAfterViewInit() {
    console.log('ngAfterViewInit - 動的要素:', this.dynamicElement);
    // 最初は要素が表示されていない場合がある
  }
  
  ngAfterViewChecked() {
    // 要素の表示状態が変わった後に呼ばれる
    if (this.dynamicElement) {
      console.log('動的要素が利用可能になりました');
    }
  }
  
  toggleElement() {
    this.showElement = !this.showElement;
  }
  
  accessElement() {
    if (this.dynamicElement) {
      this.dynamicElement.nativeElement.style.backgroundColor = 'yellow';
    } else {
      console.log('動的要素が存在しません');
    }
  }
}
```

### 安全なViewChild使用パターン
```typescript
@Component({
  selector: 'app-safe-viewchild',
  template: `
    <div #safeElement>安全な要素</div>
    <button (click)="safeAccess()">安全アクセス</button>
  `
})
export class SafeViewChildComponent implements AfterViewInit {
  @ViewChild('safeElement') safeElement?: ElementRef;
  
  ngAfterViewInit() {
    this.safeAccess();
  }
  
  safeAccess() {
    // オプショナルチェーニングで安全にアクセス
    if (this.safeElement?.nativeElement) {
      this.safeElement.nativeElement.style.border = '2px solid green';
    }
  }
}
```

## 実践的な活用例
- フォーム要素の初期化
- 動的コンテンツの制御
- アニメーションの開始

## ベストプラクティス
- ngAfterViewInit以降でViewChildを使用する
- オプショナルチェーニングを活用する
- 動的要素の存在チェックを行う

## 注意点
- ngOnInitではViewChildは未初期化
- ngAfterViewCheckedでの無限ループを避ける
- 適切なエラーハンドリングを実装する

## 関連技術
- コンポーネントライフサイクル
- エラーハンドリング
- 動的要素
- オプショナルチェーニング
