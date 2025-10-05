# #108 「@Output() データ付きイベント」

## 概要
Angular v20における@Output()でのデータ付きイベントを学びます。EventEmitterを使用して構造化されたデータを送信し、親コンポーネントで効率的に処理する方法について解説します。

## 学習目標
- データ付きイベントの定義方法を理解する
- 構造化されたデータの送信を習得する
- 効率的なデータ処理の実装方法を身につける

## 📺 画面表示用コード

```typescript
// データ付きイベントの基本
@Component({
  selector: 'app-data-event',
  standalone: true,
  template: `
    <div class="data-event">
      <button (click)="sendUserData()">ユーザーデータ送信</button>
      <button (click)="sendProductData()">商品データ送信</button>
    </div>
  `
})
export class DataEventComponent {
  @Output() dataEvent = new EventEmitter<{type: string, data: any}>();
  
  sendUserData() {
    const userData = {
      id: 1,
      name: '田中太郎',
      email: 'tanaka@example.com'
    };
    this.dataEvent.emit({ type: 'user', data: userData });
  }
  
  sendProductData() {
    const productData = {
      id: 101,
      name: 'Angular本',
      price: 3500,
      category: '書籍'
    };
    this.dataEvent.emit({ type: 'product', data: productData });
  }
}
```

```html
<!-- 親コンポーネントでの使用 -->
<app-data-event (dataEvent)="handleDataEvent($event)"></app-data-event>
```

```typescript
// 親でのデータ付きイベント処理
export class ParentComponent {
  handleDataEvent(event: {type: string, data: any}) {
    switch (event.type) {
      case 'user':
        this.processUserData(event.data);
        break;
      case 'product':
        this.processProductData(event.data);
        break;
    }
  }
}
```

## 技術ポイント

### 1. データ付きイベントの基本構造
```typescript
// 基本的なデータ付きイベント
interface DataEvent<T> {
  type: string;
  data: T;
  timestamp?: Date;
}

// 型安全なデータ付きイベント
interface TypedDataEvent<T> {
  eventType: string;
  payload: T;
  metadata: {
    timestamp: Date;
    source: string;
    version: string;
  };
}
```

### 2. EventEmitterでのデータ送信
```typescript
// 単純なデータ送信
this.eventEmitter.emit(data);

// 構造化されたデータ送信
this.eventEmitter.emit({
  type: 'custom',
  data: complexObject,
  metadata: additionalInfo
});
```

### 3. 親でのデータ受信と処理
```typescript
// 基本的な受信
(eventName)="handleEvent($event)"

// 型安全な受信
(eventName)="handleTypedEvent($event)"
```

## 実践的な活用例

### 1. フォームデータ送信コンポーネント
```typescript
// form-data-sender.component.ts
interface FormSubmissionEvent {
  formId: string;
  formData: any;
  validation: {
    isValid: boolean;
    errors: string[];
  };
  metadata: {
    timestamp: Date;
    userId?: string;
    sessionId?: string;
    formVersion: string;
  };
}

@Component({
  selector: 'app-form-data-sender',
  standalone: true,
  template: `
    <div class="form-data-sender">
      <h3>{{title}}</h3>
      
      <form (ngSubmit)="onSubmit()">
        <div class="form-group">
          <label>名前:</label>
          <input [(ngModel)]="formData.name" name="name" required>
        </div>
        
        <div class="form-group">
          <label>メール:</label>
          <input [(ngModel)]="formData.email" name="email" type="email" required>
        </div>
        
        <div class="form-group">
          <label>年齢:</label>
          <input [(ngModel)]="formData.age" name="age" type="number" min="0" required>
        </div>
        
        <button type="submit" [disabled]="!isFormValid">送信</button>
        <button type="button" (click)="saveAsDraft()">下書き保存</button>
      </form>
      
      <div *ngIf="validationErrors.length > 0" class="validation-errors">
        <h4>バリデーションエラー:</h4>
        <ul>
          <li *ngFor="let error of validationErrors">{{error}}</li>
        </ul>
      </div>
    </div>
  `,
  imports: [FormsModule]
})
export class FormDataSenderComponent {
  @Input() title: string = 'フォーム送信';
  @Input() formId: string = 'default-form';
  @Input() userId?: string;
  @Input() sessionId?: string;
  
  @Output() formSubmission = new EventEmitter<FormSubmissionEvent>();
  @Output() draftSave = new EventEmitter<FormSubmissionEvent>();
  
  formData = {
    name: '',
    email: '',
    age: 0
  };
  
  validationErrors: string[] = [];
  
  get isFormValid(): boolean {
    return this.validateForm().length === 0;
  }
  
  onSubmit() {
    const validation = this.validateForm();
    
    const event: FormSubmissionEvent = {
      formId: this.formId,
      formData: { ...this.formData },
      validation: {
        isValid: validation.length === 0,
        errors: validation
      },
      metadata: {
        timestamp: new Date(),
        userId: this.userId,
        sessionId: this.sessionId,
        formVersion: '1.0'
      }
    };
    
    this.formSubmission.emit(event);
  }
  
  saveAsDraft() {
    const validation = this.validateForm();
    
    const event: FormSubmissionEvent = {
      formId: this.formId,
      formData: { ...this.formData },
      validation: {
        isValid: validation.length === 0,
        errors: validation
      },
      metadata: {
        timestamp: new Date(),
        userId: this.userId,
        sessionId: this.sessionId,
        formVersion: '1.0'
      }
    };
    
    this.draftSave.emit(event);
  }
  
  private validateForm(): string[] {
    const errors: string[] = [];
    
    if (!this.formData.name.trim()) {
      errors.push('名前は必須です');
    }
    
    if (!this.formData.email.trim()) {
      errors.push('メールアドレスは必須です');
    } else if (!this.isValidEmail(this.formData.email)) {
      errors.push('有効なメールアドレスを入力してください');
    }
    
    if (!this.formData.age || this.formData.age < 0) {
      errors.push('有効な年齢を入力してください');
    }
    
    this.validationErrors = errors;
    return errors;
  }
  
  private isValidEmail(email: string): boolean {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }
}
```

### 2. ファイルアップロードデータイベント
```typescript
// file-upload-data.component.ts
interface FileUploadEvent {
  uploadId: string;
  files: Array<{
    name: string;
    size: number;
    type: string;
    lastModified: Date;
  }>;
  uploadProgress: {
    completed: number;
    total: number;
    percentage: number;
  };
  status: 'started' | 'progress' | 'completed' | 'error';
  metadata: {
    timestamp: Date;
    userId?: string;
    uploadType: 'single' | 'multiple';
    maxFileSize: number;
    allowedTypes: string[];
  };
  error?: {
    code: string;
    message: string;
    fileIndex?: number;
  };
}

@Component({
  selector: 'app-file-upload-data',
  standalone: true,
  template: `
    <div class="file-upload">
      <h3>{{title}}</h3>
      
      <div class="upload-area" (dragover)="onDragOver($event)" (drop)="onDrop($event)">
        <input 
          type="file" 
          #fileInput
          (change)="onFileSelect($event)"
          [multiple]="allowMultiple"
          [accept]="allowedFileTypes">
        <p>ファイルをドラッグ&ドロップするか、クリックして選択</p>
      </div>
      
      <div class="file-list" *ngIf="selectedFiles.length > 0">
        <h4>選択されたファイル:</h4>
        <div *ngFor="let file of selectedFiles; let i = index" class="file-item">
          <span>{{file.name}} ({{formatFileSize(file.size)}})</span>
          <button (click)="removeFile(i)">削除</button>
        </div>
      </div>
      
      <div class="upload-progress" *ngIf="isUploading">
        <div class="progress-bar">
          <div class="progress-fill" [style.width.%]="uploadProgress.percentage"></div>
        </div>
        <p>{{uploadProgress.completed}} / {{uploadProgress.total}} ファイル</p>
        <p>{{uploadProgress.percentage}}% 完了</p>
      </div>
      
      <div class="upload-actions">
        <button (click)="startUpload()" [disabled]="selectedFiles.length === 0 || isUploading">
          {{isUploading ? 'アップロード中...' : 'アップロード開始'}}
        </button>
        <button (click)="clearFiles()" [disabled]="isUploading">クリア</button>
      </div>
    </div>
  `
})
export class FileUploadDataComponent {
  @Input() title: string = 'ファイルアップロード';
  @Input() userId?: string;
  @Input() allowMultiple: boolean = true;
  @Input() maxFileSize: number = 10 * 1024 * 1024; // 10MB
  @Input() allowedFileTypes: string = 'image/*,application/pdf';
  
  @Output() uploadEvent = new EventEmitter<FileUploadEvent>();
  
  selectedFiles: File[] = [];
  isUploading = false;
  uploadProgress = {
    completed: 0,
    total: 0,
    percentage: 0
  };
  
  onFileSelect(event: Event) {
    const target = event.target as HTMLInputElement;
    if (target.files) {
      this.addFiles(Array.from(target.files));
    }
  }
  
  onDragOver(event: DragEvent) {
    event.preventDefault();
  }
  
  onDrop(event: DragEvent) {
    event.preventDefault();
    if (event.dataTransfer?.files) {
      this.addFiles(Array.from(event.dataTransfer.files));
    }
  }
  
  private addFiles(files: File[]) {
    const validFiles = files.filter(file => this.validateFile(file));
    
    if (this.allowMultiple) {
      this.selectedFiles.push(...validFiles);
    } else {
      this.selectedFiles = validFiles.slice(0, 1);
    }
  }
  
  private validateFile(file: File): boolean {
    // ファイルサイズチェック
    if (file.size > this.maxFileSize) {
      console.warn(`ファイル ${file.name} はサイズ制限を超えています`);
      return false;
    }
    
    // ファイルタイプチェック
    const allowedTypes = this.allowedFileTypes.split(',').map(type => type.trim());
    const isAllowedType = allowedTypes.some(type => {
      if (type.endsWith('/*')) {
        return file.type.startsWith(type.replace('/*', '/'));
      }
      return file.type === type;
    });
    
    if (!isAllowedType) {
      console.warn(`ファイル ${file.name} は許可されていないタイプです`);
      return false;
    }
    
    return true;
  }
  
  removeFile(index: number) {
    this.selectedFiles.splice(index, 1);
  }
  
  clearFiles() {
    this.selectedFiles = [];
  }
  
  async startUpload() {
    if (this.selectedFiles.length === 0) return;
    
    this.isUploading = true;
    const uploadId = this.generateUploadId();
    
    this.uploadProgress = {
      completed: 0,
      total: this.selectedFiles.length,
      percentage: 0
    };
    
    // アップロード開始イベント
    this.emitUploadEvent(uploadId, 'started');
    
    try {
      for (let i = 0; i < this.selectedFiles.length; i++) {
        const file = this.selectedFiles[i];
        
        // ファイルアップロードのシミュレーション
        await this.simulateFileUpload(file);
        
        this.uploadProgress.completed++;
        this.uploadProgress.percentage = Math.round((this.uploadProgress.completed / this.uploadProgress.total) * 100);
        
        // 進捗イベント
        this.emitUploadEvent(uploadId, 'progress');
      }
      
      // 完了イベント
      this.emitUploadEvent(uploadId, 'completed');
      
    } catch (error) {
      // エラーイベント
      this.emitUploadEvent(uploadId, 'error', {
        code: 'UPLOAD_ERROR',
        message: error instanceof Error ? error.message : 'アップロードエラー'
      });
    } finally {
      this.isUploading = false;
    }
  }
  
  private async simulateFileUpload(file: File): Promise<void> {
    // 実際のアップロード処理をシミュレート
    const delay = Math.random() * 2000 + 1000; // 1-3秒
    await new Promise(resolve => setTimeout(resolve, delay));
    
    // ランダムエラー（10%の確率）
    if (Math.random() < 0.1) {
      throw new Error(`ファイル ${file.name} のアップロードに失敗しました`);
    }
  }
  
  private emitUploadEvent(
    uploadId: string, 
    status: FileUploadEvent['status'], 
    error?: FileUploadEvent['error']
  ) {
    const event: FileUploadEvent = {
      uploadId,
      files: this.selectedFiles.map(file => ({
        name: file.name,
        size: file.size,
        type: file.type,
        lastModified: new Date(file.lastModified)
      })),
      uploadProgress: { ...this.uploadProgress },
      status,
      metadata: {
        timestamp: new Date(),
        userId: this.userId,
        uploadType: this.allowMultiple ? 'multiple' : 'single',
        maxFileSize: this.maxFileSize,
        allowedTypes: this.allowedFileTypes.split(',').map(type => type.trim())
      },
      error
    };
    
    this.uploadEvent.emit(event);
  }
  
  private generateUploadId(): string {
    return `upload_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  }
  
  formatFileSize(bytes: number): string {
    if (bytes === 0) return '0 Bytes';
    
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  }
}
```

### 3. 検索結果データイベント
```typescript
// search-results-data.component.ts
interface SearchResultEvent {
  searchId: string;
  query: string;
  results: Array<{
    id: string;
    title: string;
    description: string;
    url: string;
    score: number;
    category: string;
  }>;
  pagination: {
    currentPage: number;
    totalPages: number;
    totalResults: number;
    resultsPerPage: number;
  };
  filters: {
    category?: string;
    dateRange?: {
      from: Date;
      to: Date;
    };
    priceRange?: {
      min: number;
      max: number;
    };
  };
  metadata: {
    timestamp: Date;
    searchDuration: number;
    userId?: string;
    searchType: 'basic' | 'advanced';
  };
}

@Component({
  selector: 'app-search-results-data',
  standalone: true,
  template: `
    <div class="search-results">
      <h3>{{title}}</h3>
      
      <div class="search-form">
        <input 
          [(ngModel)]="searchQuery" 
          placeholder="検索クエリを入力"
          (keyup.enter)="performSearch()">
        <button (click)="performSearch()" [disabled]="isSearching">
          {{isSearching ? '検索中...' : '検索'}}
        </button>
      </div>
      
      <div class="search-filters">
        <select [(ngModel)]="selectedCategory">
          <option value="">すべてのカテゴリ</option>
          <option value="technology">テクノロジー</option>
          <option value="business">ビジネス</option>
          <option value="education">教育</option>
        </select>
        
        <div class="price-range">
          <label>価格範囲:</label>
          <input [(ngModel)]="minPrice" type="number" placeholder="最小価格">
          <input [(ngModel)]="maxPrice" type="number" placeholder="最大価格">
        </div>
      </div>
      
      <div class="search-info" *ngIf="lastSearchResults">
        <p>{{lastSearchResults.pagination.totalResults}} 件の結果が見つかりました</p>
        <p>検索時間: {{lastSearchResults.metadata.searchDuration}}ms</p>
      </div>
      
      <div class="results-list">
        <div *ngFor="let result of currentResults" class="result-item">
          <h4>{{result.title}}</h4>
          <p>{{result.description}}</p>
          <div class="result-meta">
            <span class="score">スコア: {{result.score}}</span>
            <span class="category">{{result.category}}</span>
            <a [href]="result.url" target="_blank">詳細を見る</a>
          </div>
        </div>
      </div>
      
      <div class="pagination" *ngIf="lastSearchResults && lastSearchResults.pagination.totalPages > 1">
        <button 
          (click)="goToPage(page)"
          *ngFor="let page of pageNumbers"
          [class.active]="page === currentPage">
          {{page}}
        </button>
      </div>
    </div>
  `,
  imports: [FormsModule]
})
export class SearchResultsDataComponent {
  @Input() title: string = '検索結果';
  @Input() userId?: string;
  
  @Output() searchResultEvent = new EventEmitter<SearchResultEvent>();
  
  searchQuery: string = '';
  selectedCategory: string = '';
  minPrice: number = 0;
  maxPrice: number = 0;
  isSearching = false;
  currentPage = 1;
  lastSearchResults: SearchResultEvent | null = null;
  
  get currentResults() {
    if (!this.lastSearchResults) return [];
    
    const start = (this.currentPage - 1) * this.lastSearchResults.pagination.resultsPerPage;
    const end = start + this.lastSearchResults.pagination.resultsPerPage;
    
    return this.lastSearchResults.results.slice(start, end);
  }
  
  get pageNumbers(): number[] {
    if (!this.lastSearchResults) return [];
    
    const totalPages = this.lastSearchResults.pagination.totalPages;
    const pages: number[] = [];
    
    for (let i = 1; i <= totalPages; i++) {
      pages.push(i);
    }
    
    return pages;
  }
  
  async performSearch() {
    if (!this.searchQuery.trim()) return;
    
    this.isSearching = true;
    const searchId = this.generateSearchId();
    const startTime = Date.now();
    
    try {
      // 検索処理のシミュレーション
      const results = await this.simulateSearch();
      const searchDuration = Date.now() - startTime;
      
      const searchEvent: SearchResultEvent = {
        searchId,
        query: this.searchQuery,
        results,
        pagination: {
          currentPage: this.currentPage,
          totalPages: Math.ceil(results.length / 10),
          totalResults: results.length,
          resultsPerPage: 10
        },
        filters: {
          category: this.selectedCategory || undefined,
          priceRange: (this.minPrice || this.maxPrice) ? {
            min: this.minPrice || 0,
            max: this.maxPrice || Infinity
          } : undefined
        },
        metadata: {
          timestamp: new Date(),
          searchDuration,
          userId: this.userId,
          searchType: this.selectedCategory || this.minPrice || this.maxPrice ? 'advanced' : 'basic'
        }
      };
      
      this.lastSearchResults = searchEvent;
      this.searchResultEvent.emit(searchEvent);
      
    } catch (error) {
      console.error('検索エラー:', error);
    } finally {
      this.isSearching = false;
    }
  }
  
  goToPage(page: number) {
    if (this.lastSearchResults && page >= 1 && page <= this.lastSearchResults.pagination.totalPages) {
      this.currentPage = page;
      this.lastSearchResults.pagination.currentPage = page;
      
      // ページ変更イベントを再送信
      this.searchResultEvent.emit(this.lastSearchResults);
    }
  }
  
  private async simulateSearch(): Promise<SearchResultEvent['results']> {
    // 検索処理のシミュレーション
    await new Promise(resolve => setTimeout(resolve, 1000 + Math.random() * 2000));
    
    const mockResults = [
      { id: '1', title: 'Angular開発ガイド', description: 'Angularを使ったWebアプリケーション開発の基礎', url: '/angular-guide', score: 0.95, category: 'technology' },
      { id: '2', title: 'TypeScript入門', description: 'TypeScriptの基本から応用まで', url: '/typescript-intro', score: 0.92, category: 'technology' },
      { id: '3', title: 'ビジネス戦略論', description: '現代ビジネスにおける戦略的思考', url: '/business-strategy', score: 0.88, category: 'business' },
      { id: '4', title: '教育心理学', description: '学習者の心理を理解する', url: '/education-psychology', score: 0.85, category: 'education' },
      { id: '5', title: 'React開発実践', description: 'Reactを使った実践的な開発手法', url: '/react-practice', score: 0.90, category: 'technology' }
    ];
    
    // フィルタリング
    let filteredResults = mockResults;
    
    if (this.selectedCategory) {
      filteredResults = filteredResults.filter(result => result.category === this.selectedCategory);
    }
    
    // クエリに基づくフィルタリング（簡易版）
    if (this.searchQuery) {
      const query = this.searchQuery.toLowerCase();
      filteredResults = filteredResults.filter(result =>
        result.title.toLowerCase().includes(query) ||
        result.description.toLowerCase().includes(query)
      );
    }
    
    return filteredResults;
  }
  
  private generateSearchId(): string {
    return `search_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  }
}
```

### 4. リアルタイムデータストリームイベント
```typescript
// realtime-data-stream.component.ts
interface DataStreamEvent {
  streamId: string;
  dataType: 'sensor' | 'log' | 'metric' | 'user_activity';
  data: Array<{
    timestamp: Date;
    value: any;
    metadata?: any;
  }>;
  streamInfo: {
    startTime: Date;
    endTime: Date;
    totalRecords: number;
    dataRate: number; // records per second
  };
  status: 'active' | 'paused' | 'stopped' | 'error';
  metadata: {
    source: string;
    version: string;
    compression?: boolean;
    encryption?: boolean;
  };
}

@Component({
  selector: 'app-realtime-data-stream',
  standalone: true,
  template: `
    <div class="realtime-data-stream">
      <h3>{{title}}</h3>
      
      <div class="stream-controls">
        <button (click)="startStream()" [disabled]="isStreamActive">
          {{isStreamActive ? 'ストリーム中...' : 'ストリーム開始'}}
        </button>
        <button (click)="pauseStream()" [disabled]="!isStreamActive || isPaused">一時停止</button>
        <button (click)="resumeStream()" [disabled]="!isStreamActive || !isPaused">再開</button>
        <button (click)="stopStream()" [disabled]="!isStreamActive">停止</button>
      </div>
      
      <div class="stream-info">
        <p>ストリームID: {{currentStreamId}}</p>
        <p>データタイプ: {{selectedDataType}}</p>
        <p>レコード数: {{totalRecords}}</p>
        <p>データレート: {{dataRate}} records/sec</p>
        <p>ステータス: {{streamStatus}}</p>
      </div>
      
      <div class="data-type-selector">
        <label>データタイプ:</label>
        <select [(ngModel)]="selectedDataType">
          <option value="sensor">センサーデータ</option>
          <option value="log">ログデータ</option>
          <option value="metric">メトリクス</option>
          <option value="user_activity">ユーザーアクティビティ</option>
        </select>
      </div>
      
      <div class="recent-data" *ngIf="recentData.length > 0">
        <h4>最新データ (最新10件):</h4>
        <div *ngFor="let item of recentData" class="data-item">
          <span class="timestamp">{{item.timestamp | date:'HH:mm:ss.SSS'}}</span>
          <span class="value">{{item.value | json}}</span>
        </div>
      </div>
    </div>
  `,
  imports: [FormsModule]
})
export class RealtimeDataStreamComponent implements OnDestroy {
  @Input() title: string = 'リアルタイムデータストリーム';
  
  @Output() streamEvent = new EventEmitter<DataStreamEvent>();
  
  selectedDataType: DataStreamEvent['dataType'] = 'sensor';
  currentStreamId: string = '';
  isStreamActive = false;
  isPaused = false;
  streamStatus: DataStreamEvent['status'] = 'stopped';
  totalRecords = 0;
  dataRate = 0;
  recentData: Array<{ timestamp: Date; value: any }> = [];
  
  private streamInterval?: number;
  private startTime?: Date;
  private recordCount = 0;
  
  ngOnDestroy() {
    this.stopStream();
  }
  
  startStream() {
    this.currentStreamId = this.generateStreamId();
    this.isStreamActive = true;
    this.isPaused = false;
    this.streamStatus = 'active';
    this.startTime = new Date();
    this.recordCount = 0;
    this.recentData = [];
    
    this.emitStreamEvent('active');
    
    // データストリームの開始
    this.streamInterval = setInterval(() => {
      if (!this.isPaused) {
        this.generateData();
      }
    }, 1000); // 1秒ごとにデータ生成
  }
  
  pauseStream() {
    this.isPaused = true;
    this.streamStatus = 'paused';
    this.emitStreamEvent('paused');
  }
  
  resumeStream() {
    this.isPaused = false;
    this.streamStatus = 'active';
    this.emitStreamEvent('active');
  }
  
  stopStream() {
    this.isStreamActive = false;
    this.isPaused = false;
    this.streamStatus = 'stopped';
    
    if (this.streamInterval) {
      clearInterval(this.streamInterval);
      this.streamInterval = undefined;
    }
    
    this.emitStreamEvent('stopped');
  }
  
  private generateData() {
    const timestamp = new Date();
    let value: any;
    
    // データタイプに応じたデータ生成
    switch (this.selectedDataType) {
      case 'sensor':
        value = {
          temperature: Math.random() * 30 + 15, // 15-45度
          humidity: Math.random() * 100, // 0-100%
          pressure: Math.random() * 1000 + 900 // 900-1900hPa
        };
        break;
      
      case 'log':
        value = {
          level: ['info', 'warning', 'error'][Math.floor(Math.random() * 3)],
          message: `Log entry ${this.recordCount + 1}`,
          source: 'application'
        };
        break;
      
      case 'metric':
        value = {
          cpu: Math.random() * 100, // 0-100%
          memory: Math.random() * 100, // 0-100%
          disk: Math.random() * 100 // 0-100%
        };
        break;
      
      case 'user_activity':
        value = {
          userId: Math.floor(Math.random() * 1000),
          action: ['login', 'logout', 'view', 'click'][Math.floor(Math.random() * 4)],
          page: `/page-${Math.floor(Math.random() * 10)}`
        };
        break;
    }
    
    const dataItem = { timestamp, value };
    this.recentData.unshift(dataItem);
    
    // 最新10件のみ保持
    if (this.recentData.length > 10) {
      this.recentData.pop();
    }
    
    this.recordCount++;
    this.totalRecords = this.recordCount;
    
    // データレートの計算
    if (this.startTime) {
      const elapsedSeconds = (Date.now() - this.startTime.getTime()) / 1000;
      this.dataRate = Math.round(this.recordCount / elapsedSeconds);
    }
    
    // データイベントの送信
    this.emitStreamEvent('active');
  }
  
  private emitStreamEvent(status: DataStreamEvent['status']) {
    const event: DataStreamEvent = {
      streamId: this.currentStreamId,
      dataType: this.selectedDataType,
      data: [...this.recentData],
      streamInfo: {
        startTime: this.startTime || new Date(),
        endTime: new Date(),
        totalRecords: this.totalRecords,
        dataRate: this.dataRate
      },
      status,
      metadata: {
        source: 'realtime-component',
        version: '1.0',
        compression: false,
        encryption: false
      }
    };
    
    this.streamEvent.emit(event);
  }
  
  private generateStreamId(): string {
    return `stream_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  }
}
```

## ベストプラクティス

1. **構造化されたデータ**: 明確なデータ構造の定義
2. **型安全性**: TypeScriptの型システムを活用
3. **メタデータ**: 追加情報の適切な管理
4. **エラーハンドリング**: エラー情報の適切な伝達

## 注意点

- 大量のデータを送信する場合はパフォーマンスを考慮
- データの構造が複雑になりすぎないよう注意
- 親コンポーネントでのデータ処理の効率性を考慮

## 関連技術
- EventEmitter
- データ構造
- 型安全性
- パフォーマンス最適化
