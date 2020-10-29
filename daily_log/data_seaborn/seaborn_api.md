# Relational plots   关系图
	relplot(,x, y, hue, size, style, data...)        
			Figure-level interface for drawing relational plots onto a FacetGrid. 
			# 用于将关系图绘制到FacetGrid上的图形级界面。
	scatterplot(* [,x,y,hue,style, size...]) 
		    Draw a scater plot with possibility of several semantic groupings.
		    # 绘制一个散点图，可能会出现多个语义分组
    lineplot(*, [,x,y,hue,size,style,data ...])
            Draw a line plot with possibility of serveral semantic groupings

# Distribution plots    分布图
	displot([data, x,y,hue, row, col ...])    
		Figure-level interface for drawing distribution plots onto a FaceGrid
		# 用于将分布图绘制到FacetGrid上的图形级界面。
	histplot([data, x,y,hue, weights, stat,...])
	    Plot univeriate or bivariate histograms to show distributions of datasets.
	    # 绘制单变量或双变量直方图以显示数据集的分布。
	kdeplot([x,y,shade,vertical,kernel, bw, ...])
	    Plot univariate or bivariate distributions using kernel density estimation.
	    # 使用核密度估计图绘制单变量或双变量分布
	ecdfplot([data, x,y,hue,weights, stat,...])
	    Plot empirical cumulative distribution functions.
	    # 绘制经验累积分布函数。    
	rugplot([x,height,axis, ax,data,y,hue,...])
	    Plot marginal distributions by drawing ticks along the x and y axes.
	    # 通过沿x和y轴绘制刻度线来绘制边际分布图
    distplot([a,bins,hist,kde,rug,fit,...])
    	DEPRECATED:Flexibly plot a univeriate distribution of observations.
    	# 已弃用：灵活地绘制观测值的统一分布。

Categorical plots    分类图
	catplot(* [,x,y,hue,data, row,col,...])
		Figure-level interface for drawing categorical plots onto a facetfrid
		# 图形级界面，用于将分类图绘制到
	stripplot(* [, x,y,hue,data,order,...])
	    Draw a scatterplot where one variable is categorical
	    # 绘制一个散点图，其中一个变量是分类的
	swarmplot(* [,x,y,hue,data,order,...])
	    Draw a categorical scatterplot with non-overlapping points.
	    # 绘制一个具有非重叠点的分类散点图。
    boxplot(* [, x,y,hue,data,order,...])
        Draw an enhanced box plot for larger datasets.
        # 为更大的数据集绘制增强的箱形图
    pointplot(* [,x,y,hue,data,order,...])
        Show point estimates and confidence intervals using scatter plot glyphs.
        # 使用散点图字形显示点估计和置信区间。
    barplot(* [, x,y, hue, data,order,...])
         Show point estimates and confidence intervals as rectangular bars.
         # 将点估计和置信区间显示为矩形条。    
     countplot(* [, x,y,hue,data,order,...])
         Show the counts of observations in each categorical bin using bars.
         # 用条形图显示每个分类箱中的观测值。


Regression plots 回归图
	implot(* [,x,y,data,hue,col,row, ...])
			Plot data and regression model fits across a FacetGrid

			# 绘制 数据和回归模型 以适合FacetGrid
    regplot(* [,x,y,data,x_estimator,...])
            Plot data and a linear regression model fit
            # 绘制数据并拟合线性回归模型
    residplot(* [,x,y,lowess,...])
            PLot the residuals of a linear regression
            # 求线性回归的残差

Matrix plots  矩阵图
	heatmap(data, * [, vmin, vmax, cmap, center,...])
			Plot rectangular data as a color-encoded matrix
			# 绘制矩形数据作为颜色编码矩阵
	clustermap(data, * [, pivot_kws, method,...])
			Plot a matrix dataset as a hierarchically-clustered heatmap.
			# 将矩阵数据集绘制为分层聚类的热图。

Multi-plot grids  多图网格
	Facet grids   多面网格
	    FaceGrid(data, * [,row, col, hue, ...])
	        Multi-plot grid for plotting conditional relationships.
	        # 用于绘制条件关系的多图网格。
	    FaceGrid.map(self,func, *args, **kwargs)
            Apply a plotting conditional relationships
            # 应用绘图条件关系
        FaceGrid.map_dataframe(self, func, *args,...)
           Like .map but passes args as strings and inserts data in kwargs.
           # 类似 .map ，但是此函数将args作为字符串传递并将数据插入kwargs。
   pair grids   配对网格
   		pairplot(data, * [, hue, hue_order, palette, ...])
   		    Plot pairwise relationshops in a dataset.
   		    # 	在数据集中绘制成对关系
   		PairGrid(data, * [, hue, hue_order, palette, ...])
   			Subplot grid for plotting pairwise relationships in a dataaset
   			# 子图网格，用于绘制数据集中的成对关系
   		PairGrid.map(self, func, **kwargs)
   		    Plot with the same function in every subplot.
   		    # 在每个子图中 绘制具有相同功能的图。
   		PairGrid.map_diag(self, func, **kwargs)
   		    Plot with a univariate function on each diagonal subplot.
   		    # 在每个对角线子图上使用单变量函数绘制。
   		PairGrid.map_offdiag(self, func, **kwargs)
   		    Plot with a bivariate function on the off-diagonal subplots
   		    # 在非对角子图上具有二元函数的图
        PariGrid.map_lower(self, func, **kwargs)
            Plot with a bivariate function on the lower diagonal subplots
            # 在下对角线子图上使用双变量函数绘制
        PairGrid.map_upper(self, func, **kwargs)
            Plot with a bivariate function on the upper diagonal subplots
            # 在上对角线子图上使用双变量函数绘制
Joint grids        联合网格
		jointplot(*[, x, y, data, kind, color, …])
				Draw a plot of two variables with bivariate and univariate graphs.
				# 用双变量和单变量图绘制两个变量的图。
		JointGrid(*[, x, y, data, height, ratio, …])
				Grid for drawing a bivariate plot with marginal univariate plots.
				# 用于绘制带有边际单变量图的二元图的网格。
		JointGrid.plot(self, joint_func, …)
				Draw the plot by passing functions for joint and marginal axes.
				# 通过传递关节轴和边缘轴的函数来绘制图。
		JointGrid.plot_joint(self, func, **kwargs)
				Draw a bivariate plot on the joint axes of the grid.
				# 在网格的关节轴上绘制一个双变量图。
		JointGrid.plot_marginals(self, func, **kwargs)
				Draw univariate plots on each marginal axes.
				# 在每个边缘轴上绘制单变量图。

Themes   主题
		set_theme([context, style, palette, font, …])
				Set multiple theme parameters in one step.
				# 一次性设置多个主题参数
		axes_style([style, rc])
				Return a parameter dict for the aesthetic style of the plots.
				# 返回图的 易于阅读的美学风格的参数字典。
		set_style([style, rc])
				Set the aesthetic style of the plots.
				#设置绘图的美学风格
		plotting_context([context, font_scale, rc])
				Return a parameter dict to scale elements of the figure.
				# 返回参数dict以缩放图形元素。
		set_context([context, font_scale, rc])
				Set the plotting context parameters.
				# 设置绘图上下文参数。
		set_color_codes([palette])
				Change how matplotlib color shorthands are interpreted.
				# 更改matplotlib颜色速记的解释方式。
		reset_defaults()
				Restore all RC params to default settings.
				# 将所有RC参数恢复为默认设置。
		reset_orig()
				Restore all RC params to original settings (respects custom rc).
				# 将所有RC参数恢复为原始设置（尊重自定义rc）
		set(*args, **kwargs)
				Alias for set_theme(), which is the preferred interface.
				# set_theme（）的别名，这是首选接口。


Color palettes     调色板
		set_palette(palette[, n_colors, desat, …])

				Set the matplotlib color cycle using a seaborn palette.
				# 使用深浅的调色板设置matplotlib颜色周期	
		color_palette([palette, n_colors, desat, …])

				Return a list of colors or continuous colormap defining a palette.
				# 返回定义调色板的颜色列表或连续颜色图。
		husl_palette([n_colors, h, s, l, as_cmap])

				Get a set of evenly spaced colors in HUSL hue space.
				# 在HUSL色相空间中获得一组均匀分布的颜色。
		hls_palette([n_colors, h, l, s, as_cmap])

				Get a set of evenly spaced colors in HLS hue space.
				# 在HLS色相空间中获得一组均匀分布的颜色。

		cubehelix_palette([n_colors, start, rot, …])

				Make a sequential palette from the cubehelix system.
				# 从cubehelix系统制作顺序调色板。
		dark_palette(color[, n_colors, reverse, …])

				Make a sequential palette that blends from dark to color.
				# 制作从深色到彩色混合的顺序调色板。
		light_palette(color[, n_colors, reverse, …])

				Make a sequential palette that blends from light to color.
				# 制作从浅色到彩色混合的顺序调色板。
		diverging_palette(h_neg, h_pos[, s, l, sep, …])

				Make a diverging palette between two HUSL colors.
				# 在两种HUSL颜色之间创建一个发散的调色板。
		blend_palette(colors[, n_colors, as_cmap, input])

				Make a palette that blends between a list of colors.
				# 制作一个在一系列颜色之间混合的调色板。
		xkcd_palette(colors)

				Make a palette with color names from the xkcd color survey.
				# 使用xkcd颜色调查中的颜色名称制作调色板。
		crayon_palette(colors)

				Make a palette with color names from Crayola crayons.
				# 使用Crayola蜡笔的颜色名称制作调色板。
		mpl_palette(name[, n_colors, as_cmap])

				Return discrete colors from a matplotlib palette.
				# 从matplotlib调色板返回不连续的颜色。

Palette widgets   面板小部件
		choose_colorbrewer_palette(data_type[, as_cmap])

				Select a palette from the ColorBrewer set.
				# 从ColorBrewer集中选择一个调色板。
		choose_cubehelix_palette([as_cmap])

				Launch an interactive widget to create a sequential cubehelix palette.
				# 启动一个交互式窗口小部件，以创建一个顺序的cubehelix调色板。
		choose_light_palette([input, as_cmap])

				Launch an interactive widget to create a light sequential palette.
				# 启动一个交互式小部件以创建一个浅色顺序调色板。
		choose_dark_palette([input, as_cmap])

				Launch an interactive widget to create a dark sequential palette.
				# 启动一个交互式小部件以创建一个黑暗的顺序调色板。
		choose_diverging_palette([as_cmap])

				Launch an interactive widget to choose a diverging color palette
				# 启动交互式小部件以选择不同的调色板

Utility functions  实用功能
		load_dataset(name[, cache, data_home])

				Load an example dataset from the online repository (requires internet).
				# 从在线存储库中加载示例数据集（需要Internet）
		get_dataset_names()

				Report available example datasets, useful for reporting issues.
				# 报告可用的示例数据集，对于报告问题很有用。
		get_data_home([data_home])

				Return a path to the cache directory for example datasets.
				# 返回示例数据集的高速缓存目录的路径。
		despine([fig, ax, top, right, left, bottom, …])

				Remove the top and right spines from plot(s).
				# 从情节中删除顶部和右侧的脊椎。
		desaturate(color, prop)

				Decrease the saturation channel of a color by some percent.
				# 将颜色的饱和度通道减少一些百分比。
		saturate(color)

				Return a fully saturated color with the same hue.
				# 返回具有相同色调的完全饱和的颜色。
		set_hls_values(color[, h, l, s])

				Independently manipulate the h, l, or s channels of a color.				
				# 独立操纵颜色的h，l或s通道。

				